#Other libs
from random import randint

#Global constants
SUITS = 4
VALUES = 13
HAND_SIZE = 5

#Classes

class Card(object):
    """A playing card"""

    def __init__(self, suit, value):
        """Setting up variables for the card"""

        self._suit = suit
        self._value = value

    def printCard(self):
        """Print info about the card"""

        rank = ""
        color = ""

        if self._value == 1:
            rank = "A"
        elif self._value < 10:
            rank = str(self._value)
        elif self._value == 10:
            rank = "T"
        elif self._value == 11:
            rank = "J"
        elif self._value == 12:
            rank = "Q"
        elif self._value == 13:
            rank = "K"
        else:
            rank = "Illegal rank"

        if self._suit == 0:
            color = "clubs"
        elif self._suit == 1:
            color = "diamonds"
        elif self._suit == 2:
            color = "hearts"
        elif self._suit == 3:
            color = "spades"
        else:
            color = "illegal suit"

        print("\t" + rank + " of " + color)

class Dealer(object):
    """A poker dealer"""

    def __init__(self):
        """Setting up variables for the dealer"""

        self._cards = list()
        self.getCards()

        self._deck = list()
        self.resetDeck()

    def getCards(self):
        """Initialize the cards with the 52 cards of a deck"""

        for s in range(SUITS):
            for v in range(VALUES):
                newCard = Card(s, v + 1)
                self._cards.append(newCard)

    def printCards(self):
        """Print the cards of the entire deck"""

        for card in self._cards:
            card.printCard()

    def printDeck(self):
        """Print the cards left in the deck"""

        for card in self._deck:
            card.printCard()

    def resetDeck(self):
        """Make _deck a copy of _cards"""

        print("Shuffling cards...")
        self._deck = list(self._cards)

    def dealHand(self):
        """Deal and display a hand from the deck"""

        hand = dealCards()
        print("\nYour hand:")
        suits = -1  #Indicates that no card has been checked yet
        ladder = list()

        for card in hand:
            card.printCard()

            #Check for flush
            if(suits < -1):
                continue
            elif(suits == -1):
                suits = card._suit
            elif(suits != card._suit):
                suits = -2 #Different suits

            #Check for straight
            if(ladder[0] = -1):
                continue
            if(card._value < )

            #Check for pairs etc.

    def dealCards(self, n = HAND_SIZE):
        """Deal and display cards from the deck."""

        hand = list()

        for i in range(n):
            hand.append(self._deck.pop(randint(0, len(self._deck) - 1)))

        return hand

    def readHand(self, hand)
