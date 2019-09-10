# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:37:40 2019

@author: Omar Belghaouti
"""
from cmpx import Complex

def main():
    # Instanciation 1
    number = Complex() # --> Real = 0, Imaginary = 0
    print(number)
    # Instanctiation 2
    number = Complex(42) # --> Real = 42, Imaginary = 0
    print(number)
    # Instanciation 3
    number = Complex(12, -3.2) # --> Real = 12, Imaginary = -1
    print(number)
    # Instanciation 4
    number = Complex(im=13.2, re=5)
    print(number)
    
    # Basic operations
    num1 = Complex(re=3, im=-2.5)
    num2 = Complex(re=4.2, im=13.2)
    # Summation
    print('({}) + ({}) = {}'.format(num1, num2, num1 + num2))
    # Substraction
    print('({}) - ({}) = {}'.format(num1, num2, num1 - num2))
    # Multiplication
    print('({}) * ({}) = {}'.format(num1, num2, num1 * num2))
    # Division
    print('({}) / ({}) = {}'.format(num1, num2, num1 / num2))
    # Floor division
    print('({}) // ({}) = {}'.format(num1, num2, num1 // num2))
    # Congugated of a complex number
    print('con({}) = {}'.format(num1, num1.con()))
    # Module of a complex number
    print('mod({}) = {}'.format(num1, num1.mod()))
    
    # Basic comparisons
    num1 = Complex(im=3.1, re=-5)
    num2 = Complex(im=-1.5, re=0.6)
    # Greater than
    if(num1 > num2): print('({}) > ({})'.format(num1, num2))
    # Greater or equal
    if(num1 >= num2): print('({}) >= ({})'.format(num1, num2))
    # Less than
    if(num1 < num2): print('({}) < ({})'.format(num1, num2))
    # Less or equal
    if(num1 <= num2): print('({}) <= ({})'.format(num1, num2))
    # Equal
    if(num1 == num2): print('({}) == ({})'.format(num1, num2))
    # Not equal
    if(num1 != num2): print('({}) != ({})'.format(num1, num2))
    
if __name__ == '__main__': main()
