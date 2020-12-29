#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:28:56 2020

@author: Simon Krzysiak


"""
import math
import card


class PokerHand(card.Hand):
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
        """Classifies the hand and prints its value."""
        
        if not hasattr(self, 'value'):
            self.classify()
        print(PokerHand.hand_names[self.value])

    def has_pair(self):
        return 2 in self.ranks.values()

    def has_two_pairs(self):
        pairs = 0
        for rank in self.ranks:
            if self.ranks[rank] == 2:
                pairs += 1
        return pairs == 2

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
        return self.has_three() and self.has_pair()

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


def estimate_probabilities(multiplier=1):
    """Estimates probabilities of the different poker hands via Monte Carlo
        simulation."""
        
    nr_combinations = 2598960  # Number of all distinct hands.
    hist = card.Hist()
    total_samples = math.floor(nr_combinations * multiplier)

    for i in range(total_samples):
        deck = card.Deck()
        deck.shuffle()
        poker = PokerHand(deck)
        poker.classify()
        hist.change_freq(poker.value, 1)

    probs = list()
    for val in hist:
        probs.append((val, (hist[val] * 100) / total_samples))
    probs.sort()
    probs.extend([(i, 0) for i in range(len(probs), 10)])

    return probs


# Driver code: estimates probabilities and prints the results.
probs = estimate_probabilities(multiplier=0.01)
for i in range(10):
    print(PokerHand.hand_names[i], probs[i][1], '%')
