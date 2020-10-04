"""
Chapter 4 Problem #1: Factor Finder

Write a program that will ask the user to input an expression, calculate its
factors, and print them. Your program should be able to handle invalid input
by making use of exception handling.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 18, 2018
"""
from sympy import factor, sympify, pprint
from sympy.core.sympify import SympifyError

if __name__ == '__main__':
    expr = input('Enter the first expression: ')

    try:
        expr = sympify(expr)
    except SympifyError:
        print('Invalid input')

    factors = factor(expr)
    pprint(factors)
