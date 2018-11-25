"""
Chapter 5 Problems #2: Law of Large Numbers

According to the la w of large numbers, the average value of results over
multiple trials approaches the expected value as the number of trials
increases. Your challenge in this task is to verify the law when rolling a six-
sided die for the following number of trials: 100, 1000, 1,0000, 10,000, 
100,000, 500,000.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 18, 2018
"""
import random

def toss_die(tosses):
    sum = 0
    for toss in range(tosses):
        sum += random.randint(1,6)
    return sum/tosses

if __name__ == '__main__':
    trials = [100, 1000, 10000, 10000, 100000, 500000]
    print('Expected value: 3.5')
    for trial in trials:
        avg = toss_die(trial)
        print('Trials: {0} Trial average {1}'.format(trial,avg))