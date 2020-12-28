#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:21:25 2020

@author: Simon Krzysiak
"""
import random
import math


class Hist(dict):
    """A histogram representing frequencies of occurrence."""

    def __init__(self, items=[]):
        """Initialise the histogram with items, each with frequency 1."""
        for item in items:
            self[item] = 1

    def change_freq(self, x, change=1):
        """Changes frequency of x by change"""
        self[x] = self.get(x, 0) + change

        """Remove the key if the frequency is no longer positive."""
        if self[x] <= 0:
            del self[x]


class Card:
    """Represents a standard playing card.
        attributes:
        rank: int 2-14
        suit: int 0-3
        """

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, None, '2', '3', '4', '5', '6', '7', '8', '9',
                  '10', 'Jack', 'Queen', 'King', 'Ace']

    def __init__(self, rank=2, suit=0):
        """Initialises a card. By default it's 2 of Clubs."""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __lt__(self, other):
        return (self.rank, self.suit) < (other.rank, other.suit)


class Deck:
    """Represents a deck of Cards.
        attributes: cards(list of Cards)"""

    def __init__(self, cards=[]):
        if cards == []:
            self.cards = list()
            for rank in range(2, 15):
                for suit in range(4):
                    card = Card(rank, suit)
                    self.cards.append(card)
        else:
            self.cards = cards

    def __str__(self):
        cards = list()
        for card in self.cards:
            cards.append(str(card))
        return '\n'.join(cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, other):
        self.cards.append(other)

    def remove_card(self, other):
        if other in self.cards:
            self.cards.remove(other)

    def pop_card(self):
        """Picks the last card from self."""
        return self.cards.pop()

    def move_cards(self, other, nr_cards):
        """Moves nr_cards from other to sef """
        for i in range(nr_cards):
            self.cards.append(other.pop_card())


class Hand(Deck):
    """Represents a playing hand of Cards.
        attributes:
        cards: list of Cards
        ranks: Hist of ranks
        suits: Hist of suits"""

    def __init__(self, cards=[]):
        if cards == []:
            self.cards = list()
        else:
            self.cards = cards

    def ranks(self):
        """Builds a histogram of ranks, stored at self.ranks."""
        self.ranks = Hist()
        for card in self.cards:
            self.ranks.change_freq(card.rank, 1)

    def suits(self):
        """Builds a histogram of suits, stored at self.suits."""
        self.suits = Hist()
        for card in self.cards:
            self.suits.change_freq(card.suit, 1)


class PokerHand(Hand):
    """Represents a poker hand. The hand is meant to have 5 cards and the
        methods are written under this assumption. Also, we assume that Ace is
        the highest rank.
        attributes:
        cards: list of Cards
        ranks: Hist of ranks
        suits: Hist of suits
        value: int 0-9 representing value of hand"""

    hand_names = ['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind',
                  'Straight', 'Flush', 'Full House', 'Four of a Kind',
                  'Straight Flush', 'Royal Flush']

    def __init__(self, deck=None):
        """Initialises a PokerHand. If deck is provided, it draws 5 cards from
        it and computes ranks and suits histograms."""
        self.cards = list()
        if deck is not None:
            self.move_cards(deck, 5)
            self.cards.sort()
            self.ranks()
            self.suits()

    def print_value(self):
        if not hasattr(self, 'value'):
            self.classify()
        print(PokerHand.hand_names[self.value])

    def has_pair(self):
        return 2 in self.ranks.values()

    def has_two_pairs(self):
        pairs = 0
        for rank in self.ranks:
            if self.ranks[rank] >= 2:
                pairs += 1
        return pairs >= 2

    def has_three(self):
        return 3 in self.ranks.values()

    def has_straight(self):
        ranks = list()
        for rank in self.ranks:
            ranks.append(rank)
        ranks.sort()
        min_rank = min(ranks)
        straight = [min_rank + i for i in range(5)]
        return ranks == straight

    def has_flush(self):
        return len(self.suits) == 1

    def has_fullhouse(self):
        return self.has_three() and self.has_two_pairs()

    def has_four(self):
        return 4 in self.ranks.values()

    def has_straight_flush(self):
        return self.has_flush() and self.has_straight()

    def has_royal_flush(self):
        return self.has_straight_flush() and max(self.ranks) == 14

    def classify(self):
        """Computes self.value by checking againt different hands in decreasing
            order of strength."""
        if self.has_royal_flush():
            self.value = 9
        elif self.has_straight_flush():
            self.value = 8
        elif self.has_four():
            self.value = 7
        elif self.has_fullhouse():
            self.value = 6
        elif self.has_flush():
            self.value = 5
        elif self.has_straight():
            self.value = 4
        elif self.has_three():
            self.value = 3
        elif self.has_two_pairs():
            self.value = 2
        elif self.has_pair():
            self.value = 1
        else:
            self.value = 0


def estimate_probabilities(multiplier=0.01):
    nr_combinations = 2598960
    hist = Hist()
    total_samples = math.floor(nr_combinations*multiplier)

    for i in range(total_samples):
        deck = Deck()
        deck.shuffle()
        poker = PokerHand(deck)
        poker.classify()
        hist.change_freq(poker.value, 1)

    probs = list()
    for val in hist:
        probs.append((val, (hist[val]*100)/total_samples))
    probs.sort()
    probs.extend([(i, 0) for i in range(len(probs), 10)])

    return probs


probs = estimate_probabilities()
for i in range(10):
    print(PokerHand.hand_names[i], probs[i][1], '%')
