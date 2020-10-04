"""
Chapter 5 Problems #3: How Many Toss Before You Run Out of Money

Let's consider a simple game played with a fair coin toss. A player wins $1 for
heads and loses $1.50 for tails. The game is over when the player's balance
reaches $0. Given a certain starting point specified by the user as input,
your challenge is to write a program that simulates this game. Assume there's
an unlimited cash reserve with the computer - your opponent here.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 18, 2018
"""
import random

if __name__ == '__main__':
    hand = float(input('Enter your starting amount: '))
    count = 0
    while hand > 0:
        count += 1
        if random.randint(0, 1) == 1:
            hand -= 1.5
            print('Tails! Current amount: {0}'.format(hand))
        else:
            hand += 1
            print('Heads! Current amount: {0}'.format(hand))
    print(
        'Game over :( Current amount: {0}. Coin tosses: {1}'.format(
            hand,
            count))
