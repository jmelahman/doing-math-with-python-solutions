"""
Chapter 5 Problems #1: Using Venn Diagrams to Visualize Relationships Between
Sets

For your challenge, imagine you've created an online questionnaire asking your
the following question: Do you play football, another sport, or no sports? Once
you have the results, create a CSV file, sports.csv, as follows:

StudentID,Football,Others
1,1,0
2,1,1
3,0,1

Create 20 such rows for the 200 students in your class. The first column is the
student ID (the survey isn't anonymous), the second colun has a 1 if the
students has marked "football" as the sport they love to play, and the third
column has a 1 if the student plays any other sport or none at all. Write a
program to create a Venn diagram to depict the summarized results of the survey
, as shown in Figure 5-5.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 18, 2018
"""
import matplotlib.pyplot as plt
#from matplotlib_venn import venn2
# I don't have scipy installed on my machine
from sympy import FiniteSet
import csv


def draw_venn(sets):
    venn2(subsets=sets)
    plt.show()


def read_csv(filename):
    football = []
    other = []
    with open(filename) as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[1] == '1':
                football.append(row[0])
            if row[2] == '1':
                other.append(row[0])

    return football, other


if __name__ == '__main__':
    football, other = read_csv('sports.csv')
    draw_venn([football, other])
