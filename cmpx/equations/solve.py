# -*- coding: utf-8 -*-
from cmpx import Complex
from cmpx import print_err
from math import sqrt

# Function to solve a second degree (or linear) equation with passing arguments seperatly
def solve(a, b, c=0):
    try:
        if a or a and b == 0 :
            raise ValueError('At least give a number to the first two coefficents')
        if c != 0:
            delta = b**2 - 4 * a * c
            if(delta < 0):
                solution = (Complex(-b/2*a, -sqrt(-delta)/2*a),
                            Complex(-b/2*a, sqrt(-delta)/2*a))
            elif(delta == 0):
                solution = (Complex(-b/2*a))
            else:
                solution = (Complex((-b - sqrt(delta))/2*a),
                            Complex((-b + sqrt(delta))/2*a))
            return solution
        else:
            return (Complex(-b/a))
    except (ZeroDivisionError, ValueError) as err:
        print_err(err)
