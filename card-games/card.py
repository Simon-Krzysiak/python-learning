#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 12:21:25 2020

@author: Simon Krzysiak
"""
import random


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
