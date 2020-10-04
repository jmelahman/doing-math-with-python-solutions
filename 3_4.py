"""
Chapter 3 Problem #4: Find the Percentile

Let's say we want to calculate the observation at percentile p:
    1. In ascending order, sort the given list of numbers, which we might call
    data.
    2. Calculate
        i = frac{np}{100}+0.5,
    where n is the number of items in data.
    3. If i is an integer, data[i] is the number corresponding to percentile p.
    4. If i is not an integer, set k equal to the integral part of i and f
    equal to the fraction part of i. The number (1-f)*data[k] + f*data[k+1] is
    the nuber at percentile p.

Using this approach, write a program that will take a set of numbers in a file
and display the number that corresponds to a specific percentile supplied as an
input to the program.


Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""


def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers


def val_for_percentile(numbers, percentile):

    i = len(numbers) * percentile / 100.0 + 0.5

    if int(i) == i:
        val = numbers[i]
        print('{0} corresponds to percentile {1}'.format(val, percentile))
    else:
        k = int(i)
        f = i - k
        val = (1 - f) * data[k] + f * data[k + 1]
        print('{0} corresponds to percentile {1}'.format(val, percentile))


if __name__ == '__main__':
    data = sorted(read_data('mydata.txt'))

    percentile = float(input('Enter the percentile: '))
    val_for_percentile(data, percentile)
