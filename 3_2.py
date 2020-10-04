"""
Chapter 3 Problem #2: Statistics Calculator

Implement a statistics calulator that takes a list of numbers in the file
mydata.txt and then calculates and prints the mean, median, mode, variance, and
standard deviation using the functions we wrote earlier in this chapter.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""
from collections import Counter


def read_data(filename):
    numbers = []
    with open(filename) as f:
        for line in f:
            numbers.append(float(line))

    return numbers


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean


def calculate_median(numbers):

    N = len(numbers)
    numbers.sort()

    # Fine the median
    if N % 2 == 0:
        # if N is even, convert to int and match position
        m1 = int(N / 2) - 1
        m2 = int((N / 2) + 1) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        # Convert to integer, match position
        m = int((N + 1) / 2) - 1
        median = numbers[m]

    return median


def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()

    max_count = numbers_freq[0][1]

    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])

    return modes


def find_differences(numbers):
    # Find the mean
    mean = calculate_mean(numbers)
    # Find the differences from the mean
    diff = []
    for num in numbers:
        diff.append(num - mean)

    return diff


def calculate_variance(numbers):
    # Find the list of differences
    diff = find_differences(numbers)
    # Find the squared differences
    squared_diff = []

    for d in diff:
        squared_diff.append(d**2)
    # Find the variance
    sum_squared_diff = sum(squared_diff)

    variance = sum_squared_diff / len(numbers)

    return variance


if __name__ == '__main__':
    data = read_data('mydata.txt')
    mean = calculate_mean(data)
    median = calculate_median(data)
    mode = calculate_mode(data)
    variance = calculate_variance(data)
    std_ev = variance**0.5
    print('Mean: {0}, Median {1}, Mode {2}'.format(mean, median, mode))
    print('Variance: {0}, Standard Deviation: {1}'.format(variance, std_ev))
