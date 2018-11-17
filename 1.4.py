#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 1 Problem #4: Fraction Calculator

Write a calculator that can perform the basic mathematical operations on two 
fractions. It should ask the user for two fractions and the operations the user
user wants to carry out. As a head start, here's how you can write the program
with only the addition operation:
    
    '''
    Fraction operations
    '''
    def add(a,b):
        print('Result of Addition: {0}'.format(a+b))

    if __name__ == '__main__':
        
        a = Fraction(input('Enter first fraction: '))

        b = Fraction(input('Enter second fraction: '))
        op = input('Operation to perform - Add, Subtract, Divide, Mulitply: ')
        if op == 'Add':
            add(a,b)
            
Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
from fractions import Fraction

def add(a,b):
        print('{0} + {1} = {2}'.format(a,b,a+b))

def subtract(a,b):
        print('{0} - {1} = {2}'.format(a,b,a-b))

def multiply(a,b):
        print('{0} * {1} = {2}'.format(a,b,a*b))

def divide(a,b):
        print('{0} / {1} = {2}'.format(a,b,a/b))

if __name__ == '__main__':
    
    a = Fraction(input('Enter first fraction: '))

    b = Fraction(input('Enter second fraction: '))
    op = str.lower(input('Operation to perform - Add, Subtract, Mulitply, Divide: '))
    if op == 'add':
        add(a,b)
    elif op == 'subtract':
        subtract(a,b)  
    elif op == 'multiply':
        multiply(a,b)  
    elif op == 'divide':
        divide(a,b)  
    else:
        print('Input a valid operation')