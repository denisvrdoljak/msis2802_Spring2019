#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 09:46:56 2018

@author: denisvrdoljak
"""


import random

class Card:
    possiblesuits = ('Spade', 'Heart', 'Diamond', 'Club')
    suitsymbols = {text: symbol for text, symbol in zip(('Spade', 'Heart', 'Diamond', 'Club'), ['\u2660', '\u2665', '\u2666', '\u2663'])}
    possiblecardvalues = [str(n) for n in range(2, 11)] + ['J', 'Q', 'K','A']

    def __init__(self,suit,cardvalue):
        if suit.title() not in self.possiblesuits:
            raise ValueError("'{}' is not a valid suit. Valid suits are -- {} -- passed in as a string".format(suit,self.possiblesuits))
        if cardvalue.upper() not in self.possiblecardvalues:
            raise ValueError("'{}' is not a valid card value. Valid suits are -- {} -- passed in as a string".format(cardvalue, self.possiblecardvalues))
        self.value = cardvalue.upper()
        self.suit = suit.title()
        self.suitsymbol = self.suitsymbols[self.suit]

    def __repr__(self):
        return '{}{}'.format(self.value, self.suitsymbol)

class Deck:
    def __init__(self):
        self.loadnewdeck()
        self.shuffledeck()

    def loadnewdeck(self):
        self.deck = list()
        for value in Card.possiblecardvalues:
            for suit in Card.possiblesuits:
                self.deck.append(Card(suit,value))

    def shuffledeck(self):
        random.shuffle(self.deck)

    def cardsleftindeck(self):
        return len(self.deck)

    def dealcard(self):
        return self.deck.pop()

if __name__ == "__main__":
    print("=== === testing deal card function=== ===")

    print("\nTesting the duck")
    myduck = Duck()
    myduck.nametheduck("Bob")
    myduck.quack()

    print("\nTesting the soccer ball")
    mysoccerball = SoccerBall()
    mysoccerball.kick()

    #random.seed(5)
    # remove seed when done testing
    print("\nTesting the card deck:")
    testdeck = Deck()
    testdeck.loadnewdeck()
    #testdeck.shuffledeck()
    print("(Dealing the whole deck)")
    while testdeck.cardsleftindeck() > 0:
        card = testdeck.dealcard()
        print(card,end=" ")

