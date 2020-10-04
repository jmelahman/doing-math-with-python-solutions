"""
Chapter 6 Problems #1: Packing Circles into a Square

In this challenge, you'll attempt a very simplified version of the "circles
packed into a square" problem. How many circles of radius 0.5 will fit in the
square preoduced by this code?

def draw_square():
    ax = plt.axes(xlim= (0,6), ylim = (0,6))
    square = plt.Polygon([(1,1), (5,1), (5,5), (1,5)], fc='b',closed = False)
    ax.add_patch(square)
    plt.show()

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
import matplotlib.pyplot as plt


def draw_shapes():
    ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)],
                         fc='b', closed=False)
    ax.add_patch(square)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = draw_circle(x, y)
            ax.add_patch(c)

            x += 1.0
        y += 1.0


def draw_circle(x, y):
    circle = plt.Circle((x, y), radius=0.5)
    return circle


if __name__ == '__main__':
    draw_shapes()
    plt.show()
