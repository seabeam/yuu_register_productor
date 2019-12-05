# uvm_reg_gen
UVM register utility generation by inputting xls table.
It has a demo template to generate uvm register, you can implement your own template for uvm block, register HTML, register FW code, RTL etc.

## Dependency
openpyxl jinja2

## License
Under Apache License, Version 2.0

## More
Feel free to contact via email: seabeam@yahoo.com

## Usage
usage: yrp.py [-h] -n MODULE_NAME -t TEMPLATE_NAME -i INPUT_XLSX [-o OUTPUT_PATH]

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
