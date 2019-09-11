# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 17:36:25 2019

@author: Omar Belghaouti
"""
from math import sqrt
# Complex class for complex number manipulations
class Complex():
    # Constructor
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im
    # Operator overloading 1 : +
    def __add__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.re + other.re, self.im + other.im)
    # Operator overloading 2 : -
    def __sub__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.re - other.re, self.im - other.im)
    # Operator overloading 3 : *
    def __mul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)
    # Operator overloading 4 : /
    def __truediv__(self, other):
        try:
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            return Complex(num.re / den.re, num.im / den.re)
        except ZeroDivisionError as err:
            print('Error: {}'.format(err))
    # Operator overloading 5 : //
    def __floordiv__(self, other):
        try:
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            return Complex(num.re // den.re, num.im // den.re)
        except ZeroDivisionError as err:
            print('Error: {}'.format(err))
    def __gt__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return self.mod() > other.mod()
    # Operator overloading 7 : >=
    def __ge__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return self.mod() >= other.mod()
    # Operator overloading 8: <
    def __lt__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return not self >= other
    # Operator overloading 9: <=
    def __le__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return not self > other
    # Operator overloading 10: ==
    def __eq__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return (self.re == other.re) and (self.im == other.im)
    # Operator overloading 11: !=
    def __ne__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        return not self == other
    # Operator overloading 12: +=
    def __iadd__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        self.re += other.re
        self.im += other.im
        return Complex(self.re, self.im)
    # Operator overloading 13: -=
    def __isub__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        self.re -= other.re
        self.im -= other.im
        return Complex(self.re, self.im)
    # Operator overloading 14: *=
    def __imul__(self, other):
        if not isinstance(other, Complex):
            other = Complex(other)
        self.re = self.re * other.re - self.im * other.im
        self.im = self.re * other.im + self.im * other.re
        return Complex(self.re, self.im)
    # Operator overloading 15: /=
    def __idiv__(self, other):
        try:
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            self.re = num.re / den.re
            self.im = num.im / den.re
            return Complex(self.re, self.im)
        except ZeroDivisionError as err:
            print('Error: {}'.format(err))
    # Operator overloading 16: //=
    def __ifloordiv__(self, other):
        try:
            if not isinstance(other, Complex):
                other = Complex(other)
            den = other * other.con()
            num = self * other.con()
            self.re = num.re // den.re
            self.im = num.im // den.re
            return Complex(self.re, self.im)
        except ZeroDivisionError as err:
            print('Error: {}'.format(err))
    ## Helper functions
    # Module function to calculate the modulus of a complex number
    def mod(self):
        return sqrt(self.re**2 + self.im**2)
    # Conjugated of a complex number
    def con(self):
        return Complex(self.re, - self.im)
    # String function
    def __str__(self):
        output = str(self.re) + ' + ' + str(self.im) + 'j' if(self.im != 0) else str(self.re)
        output = str(self.re) + ' - ' + str(-self.im) + 'j' if (self.im < 0) else output
        return output