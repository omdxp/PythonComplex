# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:36:25 2019

@author: Omar Belghaouti
"""
import os
from colorama import init, Fore, Style
from math import sqrt

# Check the os to make output colorful in any platform
if os.name == 'nt':
    init(convert=True)
elif os.name == 'linux' or 'linux2' or 'darwin':
    init(convert=False)
    
# Complex class for complex number manipulations
class Complex():
    # Constructor
    """
    re : is the real part of complex number
    im : is the imaginary part of complex number
    restore : whenever an error occurs on any operation of a complex number, the last instance will be restored (By default it's true)
    """
    def __init__(self, re=0, im=0, restore=True):
        self.re = re
        self.im = im
        self.restore = restore
    # Operator overloading 1 : +
    def __add__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 2 : -
    def __sub__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 3 : *
    def __mul__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 4 : /
    def __truediv__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            if den.re == 0 and self.restore:
                print(Fore.RED + 'Float division by zero')
                print(Fore.GREEN + 'Restoring last number')
                print(Style.RESET_ALL, end='')
                return Complex(self.re, self.im)
            return Complex(num.re / den.re, num.im / den.re)
        except (ZeroDivisionError, ValueError) as err:
            self.print_err(err)
    # Operator overloading 5 : //
    def __floordiv__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            if den.re == 0 and self.restore:
                print(Fore.RED + 'Float division by zero')
                print(Fore.GREEN + 'Restoring last number')
                print(Style.RESET_ALL, end='')
                return Complex(self.re, self.im)
            return Complex(num.re // den.re, num.im // den.re)
        except (ZeroDivisionError, ValueError) as err:
            self.print_err(err)
    def __gt__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return self.mod() > other.mod()
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 7 : >=
    def __ge__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return self.mod() >= other.mod()
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 8: <
    def __lt__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self >= other
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 9: <=
    def __le__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self > other
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 10: ==
    def __eq__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return (self.re == other.re) and (self.im == other.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 11: !=
    def __ne__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self == other
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 12: +=
    def __iadd__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re += other.re
            self.im += other.im
            return Complex(self.re, self.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 13: -=
    def __isub__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re -= other.re
            self.im -= other.im
            return Complex(self.re, self.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 14: *=
    def __imul__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re = self.re * other.re - self.im * other.im
            self.im = self.re * other.im + self.im * other.re
            return Complex(self.re, self.im)
        except ValueError as err:
            self.print_err(err)
    # Operator overloading 15: /=
    def __idiv__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            if den.re == 0 and self.restore:
                print(Fore.RED + 'Float division by zero')
                print(Fore.GREEN + 'Restoring last number')
                print(Style.RESET_ALL, end='')
                return Complex(self.re, self.im)
            self.re = num.re / den.re
            self.im = num.im / den.re
            return Complex(self.re, self.im)
        except (ZeroDivisionError, ValueError) as err:
            self.print_err(err)
    # Operator overloading 16: //=
    def __ifloordiv__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            if den.re == 0 and self.restore:
                print(Fore.RED + 'Float division by zero')
                print(Fore.GREEN + 'Restoring last number')
                print(Style.RESET_ALL, end='')
                return Complex(self.re, self.im)
            self.re = num.re // den.re
            self.im = num.im // den.re
            return Complex(self.re, self.im)
        except (ZeroDivisionError, ValueError) as err:
            self.print_err(err)
    ## Helper functions
    # Module function to calculate the modulus of a complex number
    def mod(self):
        return sqrt(self.re**2 + self.im**2)
    # Conjugated of a complex number
    def con(self):
        return Complex(self.re, - self.im)
    # function to print the error message
    def print_err(self, err):
        print(Fore.RED + '{}: {}'.format(err.__class__.__name__, err))
        print(Style.RESET_ALL, end='')
    # Representation function for representing a complex number
    def __repr__(self):
        output = str(self.re) + ' + ' + str(self.im) + 'j' if(self.im != 0) else str(self.re)
        output = str(self.re) + ' - ' + str(-self.im) + 'j' if (self.im < 0) else output
        return output