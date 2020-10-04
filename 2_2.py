"""
Chapter 2 Problem #2: Exploring a Quadratic Function Visually

Here's  program that calculates the value of y for six different values of x:
    '''
    Quadratic function calculator
    '''
    # Assume values of x

    x_values = [-1,1,2,3,4,5]

    for x in x_values:
        # Calculate the value of quadratic function
        y = x**2 + x*2 +1
        print('x={0} y{1}'.format(x,y))

Your programming challenge is to enhance this program to create a graph of the
function. Try using at least 10 values for x instead of the 6 above. Calculate
the corresponding y values using the function and then create a graph using
these two sets of values.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
import matplotlib.pyplot as plt


def quad_func_calc():
    x_values = [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    y_values = []
    for x in x_values:
        # Calculate the value of quadratic function
        y_values.append(x**2 + x * 2 + 1)
    draw_graph(x_values, y_values)


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('x-axis')

    plt.ylabel('y-axis')
    plt.title('Quadratic Function')


if __name__ == '__main__':
    quad_func_calc()
