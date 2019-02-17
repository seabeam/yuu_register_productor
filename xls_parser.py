###################################################################################
# Copyright 2019 seabeam@yahoo.com - Licensed under the Apache License, Version 2.0
# For more information, see LICENCE in the main folder
###################################################################################

from openpyxl import load_workbook
from openpyxl.utils import *

from register_node import RegisterNode, walk


class XLSParser(object):
    def get_hex(self, data):
        if isinstance(data, int):
            return "%X" %data
        try:
            int(data, 16)
            data = data.upper()
            return data[2:]
        except:
            print("Fatal: Invalid data format(%s), only decimal or hexadecimal with \
prefix '0x' supported" %(data))
        return None


    def get_sheet(self, name):
        self.sheet = load_workbook(name)['Info']


    def in_range(self, column, start, end):
        return ord(column) in range(ord(start), ord(end))


    def locate(self, start_column):
        s_row = [cell for cell in self.sheet[start_column] if cell.value == 'Block'][0].row
        s_reg = [cell for cell in self.sheet[s_row] if cell.value == 'Register'][0].column
        s_field = [cell for cell in self.sheet[s_row] if cell.value == 'Field'][0].column
        
        if isinstance(s_reg, int):
            s_reg = get_column_letter(s_reg)
        if isinstance(s_field, int):
            s_field = get_column_letter(s_field)
        return (s_row, s_reg, s_field)


    def get_header(self):
        self.header = {}
        self.header['block'] = 'A'
        self.start_row, self.header['register'], self.header['field'] = self.locate(self.header['block'])
        
        for cell in self.sheet[self.start_row]:
            if isinstance(cell.column, int):
                column = get_column_letter(cell.column)
            else:
                column = cell.column
            if cell.value == 'Offset':
                if self.in_range(column, self.header['block'], self.header['register']):
                    self.header['block_offset'] = column
                elif self.in_range(column, self.header['register'], self.header['field']):
                    self.header['reg_offset'] = column
                else:
                    print("Warning: Invalid 'Offset' column presented (Col: %s) %(column)")
            if cell.value == 'Width':
                self.header['width'] = column
            if cell.value == 'Access':
                if self.in_range(column, self.header['register'], self.header['field']):
                    self.header['reg_access'] = column
                elif self.in_range(column, self.header['field'], 'Z'):
                    self.header['field_access'] = column
                else:
                    print("Warning: Invalid 'Access' column presented (Col: %s) %(column)")
            if cell.value == 'Repeat':
                self.header['repeat'] = column
            if cell.value == 'HDL Path':
                self.header['hdl_path'] = column
            if cell.value == 'Description':
                if self.in_range(column, self.header['register'], self.header['field']):
                    self.header['reg_description'] = column
                elif self.in_range(column, self.header['field'], 'Z'):
                    self.header['field_description'] = column
                else:
                    print("Warning: Invalid 'Description' column presented (Col: %s) %(column)")
            if cell.value == 'Bits':
                self.header['bits'] = column
            if cell.value == 'Reset Value':
                self.header['reset'] = column
                    

    def parse_bits(self, field, bits):
        try:
            start = int(bits)
            field.lsb_pos = start
            field.size = 1
        except:
            bit_n =[int(x) for x in bits.split(':')]
            start = min(bit_n)
            end = max(bit_n)
            field.lsb_pos = start
            field.size = end-start+1
            

    def set_attr(self, node, key, value):
        node.attrs[key] = value
        

    def parse_data(self):
        root = RegisterNode()
        self.get_header()
        
        switch = {
            self.header['width']: lambda cell: self.set_attr(block, 'width', cell.value),
            self.header['block_offset']: lambda cell: self.set_attr(block, 'offset', '%0d\'h%s' %(block.width, self.get_hex(cell.value))),
            self.header['reg_offset']: lambda cell: self.set_attr(reg, 'offset', '%0d\'h%s' %(block.width, self.get_hex(cell.value))),
            self.header['reg_access']: lambda cell: self.set_attr(reg, 'access', cell.value),
            self.header['repeat']: lambda cell: self.set_attr(reg, 'repeat', cell.value),
            self.header['hdl_path']: lambda cell: self.set_attr(reg, 'hdl_path', cell.value),
            self.header['reg_description']: lambda cell: self.set_attr(reg, 'description', cell.value),
            self.header['bits']: lambda cell: self.parse_bits(field, cell.value),
            self.header['field_access']: lambda cell: self.set_attr(field, 'access', cell.value),
            self.header['reset']: lambda cell: self.set_attr(field, 'reset', '%0d\'h%s' %(block.width, self.get_hex(cell.value))),
        }

        for row in self.sheet[self.start_row+1:61]:
            for cell in row:
                if isinstance(cell.column, int):
                    column = get_column_letter(cell.column)
                else:
                    column = cell.column
                if cell.value == None:
                    continue
                try:
                    switch[column](cell)
                except:
                    if column == self.header['block']:
                        block = RegisterNode(cell.value)
                        root[cell.value] = block
                        continue
                    if column == self.header['register']:
                        reg = RegisterNode(cell.value)
                        block[cell.value] = reg
                        continue
                    if column == self.header['field']:
                        field = RegisterNode(cell.value)
                        reg[cell.value] = field
                        continue
        return root


def is_node(item):
    return isinstance(item, RegisterNode)
