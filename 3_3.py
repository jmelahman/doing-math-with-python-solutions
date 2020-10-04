"""
Chapter 3 Problem #3: Experiment with Other CSV Data

For this challenge, download the following data as a CSV file from
http://quandl.com/WORLDBANK/US_SP_POP_TOTL/: the total population of the
United States at the end of each year for the years 1960 to 2012. Then,
calculate the mean, median, variance, and standard deviation of the
difference in population over the years and create a graph showing these
differences.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""

"""
Chapter 3 Problem #2: Statistics Calculator

Implement a statistics calulator that takes a list of numbers in the file
mydata.txt and then calculates and prints the mean, median, mode, variance, and
standard deviation using the functions we wrote earlier in this chapter.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 17, 2018
"""




import matplotlib.pyplot as plt
from collections import Counter
import csv
def read_data_csv(filename):
    x = []
    y = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            x.append(int(row[0]))
            y.append(int(row[1]))

    return x, y


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s / N

    return mean


def calculate_median(numbers):

    N = len(numbers)
    numbers.sort()

    # Find the median
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


def draw_graph(x, y):
    plt.plot(x, y, marker='o')
    plt.xlabel('x-axis')

    plt.ylabel('y-axis')
    plt.title('Quadratic Function')


if __name__ == '__main__':
    year, pop = read_data_csv('fake_us_pop.csv')
    difference = []
    end_year = []
    for i in range(1, len(year)):
        difference.append(pop[i] - pop[i - 1])
        end_year.append(year[i])
    draw_graph(end_year, difference)
    mean = calculate_mean(difference)
    median = calculate_median(difference)
    variance = calculate_variance(difference)
    std_ev = variance**0.5
    print('Mean: {0}, Median {1}'.format(mean, median))
    print('Variance: {0}, Standard Deviation: {1}'.format(variance, std_ev))
