# -*- coding: utf-8 -*-
from math import sqrt

def delta(a, b, c):
    delta = b**2 - 4 * a * c
    if(delta < 0):
        solution = [Complex(-b/2*a, -sqrt(delta)/2*a),
                    Complex(-b/2*a, sqrt(delta)/2*a)]
    elif(delta == 0):
        solution = Complex(-b/2*a)
    else:
        solution = [Complex((-b - sqrt(delta))/2*a),
                    Complex((-b + sqrt(delta))/2*a)]
    return solution

