"""
Chapter 6 Problems #3: Exploring Henon's Function

Your challenge here is to write a program to create a graph showing 20,000 
iteractions of this transformation, starting with the point (1,1).

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
import matplotlib.pyplot as plt

def transform(p):
    x = p[0]
    y = p[1]
    x1 = y+1 - 1.4*x**2
    y1 = 0.3 * x
    return x1, y1

def draw_henon(n):
    # We start with (0,0)
    x = [1]
    y = [1]
    
    x1,y1 = 1,1
    for i in range(n):
        x1, y1 = transform((x1, y1))
        x.append(x1)
        y.append(y1)
    return x,y

if __name__ == '__main__':
    n = 20000
    x, y = draw_henon(n)
    # Plot the points
    plt.plot(x, y, 'o')
    plt.title('Henon\'s functions with 20,000 points')
    plt.show()