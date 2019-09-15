# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:36:25 2019

@author: Omar Belghaouti
"""
from colorama import Fore, Style
from .error import print_err
from math import sqrt
    
# Complex class for complex number manipulations
class Complex():
    # Constructor
    """
    re : is the real part of complex number
    im : is the imaginary part of complex number
    restore : whenever an error occurs on any operation of a complex number, the last instance will be restored (By default it's true)
    """
    def __init__(self, re=0, im=0, restore=True):
        try:
            if not ((isinstance(re, int) or isinstance(re, float)) and (isinstance(im, int) or isinstance(im, float))):
                raise ValueError('Arguments re and im arguments are neither integers nor floats')
            if not isinstance(restore, bool):
                raise ValueError('Argument restore is not boolean')
            self.re = re
            self.im = im
            self.restore = restore
        except ValueError as err:
            print_err(err)
    """
    This method instanciate a Complex object from a complex number
    """
    @classmethod
    def fromComplex(self, comp, restore=True):
        try:
            if isinstance(comp, complex):
                self.re = comp.real
                self.im = comp.imag
                self.restore = restore
            else:
                raise ValueError('The number you passed is not a complex')
        except ValueError as err:
            print_err(err)
    # Getters
    @property
    def re(self):
        return self.re
    @property
    def im(self):
        return self.im
    @property
    def restore(self):
        return self.restore
    # Setters
    @re.setter
    def re(self, re):
        self.re = re
    @im.setter
    def im(self, im):
        self.im = im
    @restore.setter
    def restore(self, restore):
        self.restore = restore
    # Deleters
    @re.deleter
    def re(self):
        del self.re
    @im.deleter
    def im(self):
        del self.im
    @restore.deleter
    def restore(self):
        del self.restore
    # Operator overloading 1 : +
    def __add__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re + other.re, self.im + other.im, self.restore)
        except ValueError as err:
            print_err(err)
    # Operator overloading 2 : -
    def __sub__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re - other.re, self.im - other.im, self.restore)
        except ValueError as err:
            print_err(err)
    # Operator overloading 3 : *
    def __mul__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re, self.restore)
        except ValueError as err:
            print_err(err)
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
                return Complex(self.re, self.im, self.restore)
            return Complex(num.re / den.re, num.im / den.re, self.restore)
        except (ZeroDivisionError, ValueError) as err:
            print_err(err)
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
                return Complex(self.re, self.im, self.restore)
            return Complex(num.re // den.re, num.im // den.re, self.restore)
        except (ZeroDivisionError, ValueError) as err:
            print_err(err)
    def __gt__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return self.mod() > other.mod()
        except ValueError as err:
            print_err(err)
    # Operator overloading 7 : >=
    def __ge__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return self.mod() >= other.mod()
        except ValueError as err:
            print_err(err)
    # Operator overloading 8: <
    def __lt__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self >= other
        except ValueError as err:
            print_err(err)
    # Operator overloading 9: <=
    def __le__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self > other
        except ValueError as err:
            print_err(err)
    # Operator overloading 10: ==
    def __eq__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return (self.re == other.re) and (self.im == other.im)
        except ValueError as err:
            print_err(err)
    # Operator overloading 11: !=
    def __ne__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            return not self == other
        except ValueError as err:
            print_err(err)
    # Operator overloading 12: +=
    def __iadd__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re += other.re
            self.im += other.im
            return Complex(self.re, self.im, self.restore)
        except ValueError as err:
            print_err(err)
    # Operator overloading 13: -=
    def __isub__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re -= other.re
            self.im -= other.im
            return Complex(self.re, self.im, self.restore)
        except ValueError as err:
            print_err(err)
    # Operator overloading 14: *=
    def __imul__(self, other):
        try:
            if other is None:
                raise ValueError('The second number is None')
            if not isinstance(other, Complex):
                other = Complex(other)
            self.re = self.re * other.re - self.im * other.im
            self.im = self.re * other.im + self.im * other.re
            return Complex(self.re, self.im, self.restore)
        except ValueError as err:
            print_err(err)
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
                return Complex(self.re, self.im, self.restore)
            self.re = num.re / den.re
            self.im = num.im / den.re
            return Complex(self.re, self.im, self.restore)
        except (ZeroDivisionError, ValueError) as err:
            print_err(err)
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
                return Complex(self.re, self.im, self.restore)
            self.re = num.re // den.re
            self.im = num.im // den.re
            return Complex(self.re, self.im, self.restore)
        except (ZeroDivisionError, ValueError) as err:
            print_err(err)
    # Operator overloading 17: - (Unary operator)
    def __neg__(self):
        return Complex(-self.re, -self.im, self.restore)
    ## Helper functions
    # Module function to calculate the modulus of a complex number
    def mod(self):
        return sqrt(self.re**2 + self.im**2)
    # Conjugated of a complex number
    def con(self):
        return Complex(self.re, - self.im, self.restore)
    # Representation function for representing a complex number
    def __repr__(self):
        if(self.re != 0 and self.im > 0):
            output = str(self.re) + ' + ' + str(self.im) + 'j' if(self.im != 1) else str(self.re) + ' + ' + 'j'
        if(self.re != 0 and self.im < 0):
            output = str(self.re) + ' - ' + str(-self.im) + 'j' if(self.im != -1) else str(self.re) + ' - ' + 'j'
        if(self.re != 0 and self.im == 0):
            output = str(self.re)
        if(self.re == 0 and self.im > 0):
            output = str(self.im) + 'j' if(self.im != 1) else 'j'
        if(self.re == 0 and self.im < 0):
            output = str(self.im) + 'j' if(self.im != -1) else '-j'
        return output