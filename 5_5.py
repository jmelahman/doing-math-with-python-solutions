#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Chapter 5 Problem #5: Estimating the Area of a Circle

As a part of this challenge, write a program that will find the estimated area
of a circle, given any radius, using this approach. The program should print
the estimated area of the circle for three different values of the number of
darts: 10^3, 10^5, and 10^6. Here's a sample output of the completed solution:

Radius: 2
Area: 12.566370614359172, Estimated (1000 darts): 12.576
Area: 12.566370614359172, Estimated (100000 darts): 12.58176

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 26, 2018
"""
import math
import random


def estimate_area(r, n):
    square_area = 4 * r**2
    count = 0
    for i in range(n):
        p = (random.uniform(-r, r), random.uniform(-r, r))
        if math.sqrt(p[0]**2 + p[1]**2) <= r:
            count += 1
    return count / n * square_area


if __name__ == '__main__':
    darts = [1000, 100000, 1000000]

    r = float(input('Radius: '))

    for n in darts:
        area = estimate_area(r, n)
        print(
            'Area: {0}, Estimated ({1} darts): {2}'.format(
                math.pi * r**2, n, area))
