#!/usr/bin/env python3
###################################################################################
# Copyright 2019 seabeam@yahoo.com - Licensed under the Apache License, Version 2.0
# For more information, see LICENCE in the main folder
###################################################################################
import os
import shutil
import argparse

from openpyxl import load_workbook
from jinja2 import Environment, FileSystemLoader

from register_node import RegisterNode, walk
from xls_parser import XLSParser, get_bit_reset, format_hex


if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description="Register utils generator for DFV")
    arg_parser.add_argument('-n', '--name', required=True, dest='module_name', help='[Required] Expected module name')
    arg_parser.add_argument('-t', '--template', required=True, dest='template_name', help='[Required] Template name, file extension should be .j2')
    arg_parser.add_argument('-i', '--input', required=True, dest='input_xlsx', help='[Required] xlsx file for generator input')
    arg_parser.add_argument('-o', '--output', required=False, dest='output_path', default='./', help='[Optional] Output path, current path by default')
    arg_parser.add_argument('-f', '--factory', required=False, dest='use_factory', action="store_true", help='[Optional] Use UVM factory')
    arg_parser.add_argument('-c', '--coverage', required=False, dest='use_coveage', action="store_true", help='[Optional] Use functional coverage')

    args = arg_parser.parse_args()
    script_dir = os.path.dirname(os.path.abspath(__file__))

    parser = XLSParser()
    parser.get_sheet('%s' %(args.input_xlsx))

    template_dir = '%s/template' %(script_dir)
    env = Environment(loader=FileSystemLoader(template_dir))
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.filters['get_bit_reset'] = get_bit_reset
    env.filters['format_hex'] = format_hex
    template = env.get_template(args.template_name)

    root = parser.parse_data()

    if not os.path.isdir('%s' %args.output_path):
        print("Output folder (%s) cannot be reached" %(args.output_path))
        exit(1)

    if args.use_factory:
        para_factory = True
    else:
        para_factory = False
    
    if args.use_coveage:
        para_coverage = "UVM_CVR_ALL"
    else:
        para_coverage = "UVM_NO_COVERAGE"

    if args.template_name == 'html.j2':
        root = parser.fill_reserved(root)
        root = parser.reorder_by_lsb(root)
        with open('%s/%s.htm' %(args.output_path, args.module_name), 'w', encoding='UTF-8') as f:
            src = "%s/html" %(script_dir)
            des = "%s/html_%s" %(args.output_path, args.module_name)
            if os.path.isdir(des):
                shutil.rmtree(des)
            shutil.copytree(src, des)
            f.write(template.render(module=args.module_name, root=root))
    elif args.template_name == 'uvm_reg_model.j2':
        with open('%s/%s_ral_model.sv' %(args.output_path, args.module_name), 'w', encoding='UTF-8') as f:
            f.write(template.render(module=args.module_name, root=root, width=32, factory=para_factory, coverage=para_coverage))
    
    print("Register productor generate done")