"""
Chapter 1 Problem #1: Even-Odd Vending Machine

Try writing an “even-odd vending machine,” which will take a number as input
and do two things

1. Print whether the number is even or odd.
2. Display the number followed by the next 9 even or odd numbers.
If the input is 2, the program should print even and then print 2, 4, 6, 8, 10,
 12, 14, 16, 18, 20. Similarly, if the input is 1, the program should print odd
and then print 1, 3, 5, 7, 9, 11, 13, 15, 17, 19. Your program should use the
is_integer() method to display an error message if the input is a number with
significant digits beyond the decimal point.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, October 24, 2018
"""


def even_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    for i in range(0, 20, 2):
        print(num + i)
    return()


def even_odd_unnecessary(num):
    # Same function as even_odd but with unnecessary print() formatting just
    # because
    print("even") if num % 2 == 0 else print("odd")
    for i in range(0, 18, 2):
        print(num + i, sep='', end=', ', flush=True)
    print(num + 18, sep='', end='.\n', flush=False)
    return()


if __name__ == '__main__':
    even_odd(2)

    even_odd_unnecessary(2)
    even_odd_unnecessary(9)
