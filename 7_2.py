"""
Chapter 7 Problem #2: Implement the Gradient Descent

Your challenge is to implement a generic prgram using the gradient
descent algorithm to find the minimum value of a single-variable
function specified as input by the user. The program should also create
a graph of the function and show all the intermediate values it found
befire finding the minimum.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
from sympy import Derivative, Symbol, sympify
from sympy.core.sympify import SympifyError

def grad_descent(x0, f1x, x):
	epsilon = 1e-6
	step_size = 1e-4
	x_old = x0
	x_new = x_old - step_size*f1x.subs({x:x_old}).evalf()
	while abs(x_old - x_new) > epsilon:
		x_old = x_new
		x_new = x_old - step_size*f1x.subs({x:x_old}).evalf()

	return x_new

if __name__ == '__main__':
	f = input('Enter a function in one variable: ')
	var = input('Enter the variable to differentiate with respect to: ')
	var0 = float(input('Enter the initial value of the variable: '))
	try:
		f = sympify(f)
	except SympifyError:
		print('Invalid function entered')
	else:

		var = Symbol(var)
		d = Derivative(f, var).doit()

		var_min = grad_descent(var0, d, var)
		print('{0}: {1}'.format(var.name, var_min))
		print('Minimum value: {0}'.format(f.subs({var:var_min})))
