"""
Chapter 7 Problem #1: Verify the Continuity of a Function at a Point

Your challenge here is to write a program that will (1) accept a single-
variable function and a value as inputs and (2) check whether the input
function is continuous at the point where the variable assumes the value
input.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
from sympy import Limit, Symbol, sympify
from sympy.core.sympify import SympifyError

def check_cont(x0, fx, x):
	right_lim = Limit(fx, x, x0).doit()
	left_lim = Limit(fx, x, x0, dir='-').doit()
	fx0 = fx.subs({x:x0})

	if fx0 == left_lim == right_lim:
		return True

if __name__ == '__main__':
	f = input('Enter a function in one variable: ')
	var = input('Enter the variable to differentiate with respect to: ')
	var0 = float(input('Enter the initial value of the variable: '))
	try:
		f = sympify(f)
	except SympifyError:
		print('Invalid function entered')

	var = Symbol(var)

	is_cont = check_cont(var0, f, var)
	if is_cont:
		print('{0} is continuous at {1}'.format(f, var0))
	else:
		print('{0} is not continuous at {1}'.format(f, var0))
