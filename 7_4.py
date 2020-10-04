#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 7 Problem #4: Finding the Length of a Curve

For this challenge, let's assume that the equation is y = f(x) = 2x**2 + 3x + 1
and that you cycled from point A(-5, 36) to point B(10, 231). To find the
length of this arc - that is, the distance you cycled - we'll need to calculate
the length of the arc, AB.

You may also want to generalize your solution so that it allows you to find the
length of that arc between any two points for any arbitrary function, f(x).

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 26, 2018
"""
from sympy import Integral, Derivative, Symbol, sympify, sqrt
from sympy.core.sympify import SympifyError


def find_arc(fx, x, a, b):
    x = Symbol('x')
    f1x = Derivative(fx, x).doit()
    arc = Integral(sqrt(1 + f1x**2), (x, a, b)).doit().evalf()
    return arc


if __name__ == '__main__':
    f = input('Enter the approxiamte function in one variable: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:

        var = input('Enter the variable to differentiate with respect to: ')
        a = input('Enter the starting position along x-axis: ')
        b = input('Enter the final position along x-axis: ')

        dist = find_arc(f, var, a, b)

        print('Total distance traveled: {0}'.format(dist))
