"""
Chapter 5 Problems #4: Shuffling a Deck of Cards

Create a list, x, consisting of the numbers [1,2,3,4]. Then, call the shuffle()
function(), passing this list as an argument. You'll see that the numbers in x
have been shuffled. Note, that the list is shiffled "in place." The is, the
original order is lost.

But what if you wanted to use this program in a card game?There, it's not
enough to simply output the shuffled list of integers. You'll also need a way
to map back the integers to the specific suit and rank of each card.

Doing Math with Python by Amit Saha

Solution by Jamison Lahman, November 23, 2018
"""
import random


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


def initialize_deck():
    deck = []
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    ranks = [
        '2',
        '3',
        '4',
        '5',
        '6',
        '7',
        '8',
        '9',
        '10',
        'jack',
        'queen',
        'king',
        'ace',
    ]
    for suit in suits:
        for rank in ranks:
            card = Card(suit, rank)
            deck.append(card)
    return deck


if __name__ == '__main__':
    deck = initialize_deck()
    random.shuffle(deck)
    for card in deck:
        print('{0} of {1}'.format(card.rank, card.suit))
