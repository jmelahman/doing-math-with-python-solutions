"""
Chapter 7 Problem #3: Area Between Two Curves

Your challenge here is to write a program that will allow the user to input any
two single-variable functions of x and print the enclosed area between the two.
The program should make it clear that the first function entered should be the
upper function, and it should also ask the for the values of x between which to
find the area.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 26, 2018
"""
from sympy import Integral, Symbol, sympify
from sympy.core.sympify import SympifyError


def find_area_between(fx, gx, x, a, b):
    x = Symbol('x')
    area = Integral(fx - gx, (x, a, b)).doit()
    return area


if __name__ == '__main__':
    f = input('Enter the upper function in one variable: ')
    try:
        f = sympify(f)
    except SympifyError:
        print('Invalid function entered')
    else:
        g = input('Enter the lower function in one variable: ')
        try:
            g = sympify(g)
        except SympifyError:
            print('Invalid function entered')
        else:
            var = input(
                'Enter the variable to differentiate with respect to: ')
            a = float(input('Enter the lower point of intersection: '))
            b = float(input('Enter the upper point of intersection: '))

            area = find_area_between(f, g, a, b)

            print(
                'The enclosed area between {0} and {1} is {2}'.format(
                    f, g, area))
