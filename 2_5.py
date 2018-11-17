"""
Chapter 2 Problem #5: Exploring the Relationship Between the Fibonacci 
Sequence and the Golden Ratio.

For this challenge, write a program that will plot on a graph the ratio between
consecutive Fibonacci numbers for, say, 100 numbers, which will demonstrate
that the values approach the golden ratio.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
import matplotlib.pyplot as plt

def draw_fibo(n):
    ratio = []
    num = []

    # Starting values
    a = 0
    b = 1    
    for i in range(1,n):
        c = a + b    
        num.append(i)
        ratio.append(c/b)
        a = b
        b = c
    draw_graph(num,ratio)
    
def draw_graph(x,y):
    plt.plot(x, y)
    plt.xlabel('No.')
    
    plt.ylabel('Ratio')
    plt.title('Ratio between consecutive Fibonacci numbers')

if __name__ == '__main__':
    draw_fibo(100)