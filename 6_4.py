#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 6 Problem #4: Drawing the Mandelbrot Set

Your challenge here is to write a program to draw the Mandelbrot Set.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 26, 2018
"""
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random


def initialize_image(x_p, y_p):
    image = []
    for i in range(y_p):
        x_colors = []
        for j in range(x_p):
            x_colors.append(0)
        image.append(x_colors)
    return image


def color_mandelbrot():
    x0, x1 = -2.5, 1.0
    y0, y1 = -1.0, 1.0
    x_p = 400
    y_p = 400
    max_iteration = 1000

    image = initialize_image(x_p, y_p)

    dx = (x1 - x0) / (x_p - 1)
    dy = (y1 - y0) / (y_p - 1)
    x = [x0 + i * dx for i in range(x_p)]
    y = [y0 + i * dy for i in range(y_p)]

    for k, xk in enumerate(x):
        for i, yi in enumerate(y):
            z = complex(0, 0)
            c = complex(xk, yi)
            iteration = 0
            while (iteration < max_iteration and abs(z) < 2):
                iteration += 1
                z = z**2 + c

            image[i][k] = iteration

    plt.imshow(image, origin='lower', extent=(x0, x1, y0, y1), cmap=cm.Greys_r,
               interpolation='nearest')
    plt.colorbar()
    plt.show()


if __name__ == '__main__':
    color_mandelbrot()
