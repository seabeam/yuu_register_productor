###################################################################################
# Copyright 2019 seabeam@yahoo.com - Licensed under the Apache License, Version 2.0
# For more information, see LICENCE in the main folder
###################################################################################

from openpyxl import load_workbook
from jinja2 import Environment, FileSystemLoader

from register_node import RegisterNode, walk
from xls_parser import XLSParser


if __name__ == '__main__':
    parser = XLSParser()
    parser.get_sheet('reg.xlsx')

    template_dir = './template'
    env = Environment(loader=FileSystemLoader(template_dir))
    env.trim_blocks = True
    env.lstrip_blocks = True
    template = env.get_template('uvm_reg_tpl.svh')

    root=parser.parse_data()
    print(template.render(module='example', root=root))
