#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 13:39:13 2020

@author: Simon Krzysiak
"""

import card
import random
import copy


class BlackJackHand(card.Hand):
    """Represents a BlackJack playing hand of Cards.
        attributes:
            cards: list of Cards
            value: non-negative int
    """

    def __init__(self, cards=[]):
        if cards == []:
            self.cards = list()
        else:
            self.cards = cards
        self.cmpt_value()

    def cmpt_value(self):
        val = 0
        for crd in self.cards:
            if crd.rank <= 10:
                val += crd.rank
            elif 11 <= crd.rank <= 13:
                val += 10
            else:
                """Dealing with variable value of aces will be
                implemented later"""
                val += 11

        self.value = val

    def compare(self, other):
        """This method compares 2 blacjack hands. Self is a priviliged hand
        (meant to be the dealer's hand). We will refer to self as dealer and
         to other as player. The rules for comparison are as follows:
             - if player has exactly 21, player wins
             - if player has more than 21, dealer wins
             - if dealer has more than 21 but player doesnt, player wins
             - otherwise higher value wins

            Dealing with variable value of aces will be implemented later."""
        self.cmpt_value()
        other.cmpt_value()
        val1 = self.value
        val2 = other.value

        if val2 > 21:
            return 1
        elif val2 == 21:
            return -1
        elif val1 > 21:
            return -1
        elif val1 == val2:
            return 0
        elif val1 > val2:
            return 1
        else:
            return -1


class Player:
    """Represents a (non-dealer) player of blackjack.
        attributes:
            hand: BlackJackHand
            money: non-negative int
            bet: non-negative int, <= money
            target: non-negative int > money
    """

    def __init__(self, money=0, target=0):
        self.hand = BlackJackHand()
        self.money = money
        self.bet = 0
        if target == 0:
            self.target = 2 * money
        else:
            self.target = target

    def __str__(self):
        out = list()
        out.append('Player with:\n')
        out.append(str(self.money) + ' money,\n')
        out.append(str(self.bet) + ' bet,\n')
        out.append(str(self.hand.value) + ' hand value.')
        
        return ''.join(out)

    def place_bet(self):
        self.bet = random.randint(1, max(self.money // 2, 1))
        
    def play_round(self, deck):
        self.hand = BlackJackHand()
        self.place_bet()
        
        while self.hand.value < 17:
            self.hand.move_cards(deck, 1)
            self.hand.cmpt_value()

        
class Dealer:
    """Represents a dealer of a blackjack game.
        attributes:
            hand: BlackJackHand
            profit: int"""
            
    def __init__(self):
        self.hand = BlackJackHand()
        self.profit = 0
        
    def winnings(self, players, crd=None):
        hand = copy.deepcopy(self.hand)
        if crd is not None:
            hand.add_card(copy.deepcopy(crd))
        total = 0
        for player in players:
            total += (player.bet * hand.compare(player.hand))
        return total
    
    def play_round(self, players, deck):
        
        self.hand = BlackJackHand()
        self.hand.move_cards(deck, 1)

        while True:
            self.hand.move_cards(deck, 1)
            self.hand.cmpt_value()
            curr_gain = self.winnings(players)
            if self.hand.value > 20:
                break

            pot_gain = 0
            for crd in deck.cards:
                pot_gain += (self.winnings(players, crd) - curr_gain)
            if pot_gain < 0:
                break

            self.hand.cmpt_value()
        self.profit += curr_gain
            
                
class Game:
    """Represents a game of blackjack.
        attributes:
            players: list of Players
            dealer: Dealer"""
    
    def __init__(self, players=[]):
        if players == []:
            self.players = list()
        else:
            self.players = players
        self.dealer = Dealer()
    
    def add_player(self, player):
        self.players.append(player)
        
    def add_players(self, players):
        self.players.extend(players)
    
    def remove_player(self, player):
        self.players.remove(player)
    
    def play_round(self):
        deck = card.Deck()
        deck.shuffle()
        for player in self.players:
            player.play_round(deck)
        self.dealer.play_round(self.players, deck)
        for player in self.players:
            player.money -= (player.bet * self.dealer.hand.compare(player.hand))
            if player.money == 0 or player.money >= player.target:
                self.remove_player(player)
    
    def play(self, limit=1000):
        counter = 0
        while self.players and counter < limit:
            self.play_round()
            counter += 1

            
# driver code
def test():
    player1 = Player(100)
    player2 = Player(100)
    player3 = Player(100)
    game = Game([player1, player2, player3])
    game.play_round()
    for player in game.players:
        print(player.money, player.bet, player.hand.value)
    print("dealer:", game.dealer.hand.value)
    print(game.dealer.winnings(game.players))
    print("Profit:", game.dealer.profit)


def test2():
    player1 = Player(100)
    player2 = Player(100)
    player3 = Player(100)
    game = Game([player1, player2, player3])
    game.play()
    return game.dealer.profit


def test3():
    return sum([test2() for _ in range(100)])
