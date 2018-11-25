"""
Chapter 6 Problems #2: Drawing the Sierpinski Triangle

Your challenge here is to write a program that draws the Sierpinski triangle
composed of a certain number of points specifid as input.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
import matplotlib.pyplot as plt
import random

def transformation_1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1
    
def transformation_2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1

def transformation_3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1

def transform(p):
    # List of transformations functions
    transformations = [transformation_1, transformation_2, transformation_3]

    # Pick random transformation function and call it
    t = random.choice(transformations)
    x,y = t(p)
    return x,y

def draw_sierpinski(n):
    # We start with (0,0)
    x = [0]
    y = [0]
    
    x1,y1 = 0,0
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x,y
        
if __name__ == '__main__':
    n = int(input('Enter the number of points in the triangle: '))
    x, y = draw_sierpinski(n)
    # Plot the points
    plt.plot(x, y, 'o')
    plt.title('Sierpinski triangle with {0} points',format(n))
    plt.show()