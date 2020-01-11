# yuu_register_productor
Register utility by inputting xls table.
It has a full template to generate uvm register, register HTML. You can implement your own template for register FW code, RTL etc.

## Dependency
openpyxl jinja2

## License
Under Apache License, Version 2.0

## NOTICE
For HTML5 code exist in HTML template, only new version of browser supported(Bug have exclude Chrome)

## More
Feel free to contact via email: seabeam@yahoo.com

## Usage
usage: yrp.py [-h] -n MODULE_NAME -t TEMPLATE_NAME -i INPUT_XLSX  
　　　　　　[-o OUTPUT_PATH] [-f] [-c]

Register utils generator for DFV

optional arguments:  
　-h, --help　　　　　　show this help message and exit  
　-n MODULE_NAME, --name MODULE_NAME  
　　　　　　　　　　　　[Required] Expected module name  
　-t TEMPLATE_NAME, --template TEMPLATE_NAME  
　　　　　　　　　　　　[Required] Template name, file extension should be .j2  
　-i INPUT_XLSX, --input INPUT_XLSX  
　　　　　　　　　　　　[Required] xlsx file for generator input  
　-o OUTPUT_PATH, --output OUTPUT_PATH  
　　　　　　　　　　　　[Optional] Output path, current path by default  
　-f, --factory  
　　　　　　　　　　　　[Optional] Use UVM factory  
　-c, --coverage  
　　　　　　　　　　　　[Optional] Use functional coverage  
