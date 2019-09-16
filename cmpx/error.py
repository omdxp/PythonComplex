# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 12:04:55 2019

@author: Cds
"""
import os
from colorama import init, Fore, Style

# Check the os to make output colorful in any platform
if os.name == 'nt':
    init(convert=True)
elif os.name == 'linux' or 'linux2' or 'darwin':
    init(convert=False)
    
# function to print the error message
def print_err(err):
    print(Fore.RED + '{}: {}'.format(err.__class__.__name__, err))
    print(Style.RESET_ALL, end='')
    
# function to print whenever restore is true
def print_res():
    print(Fore.RED + 'Float division by zero')
    print(Fore.GREEN + 'Restoring last number')
    print(Style.RESET_ALL, end='')