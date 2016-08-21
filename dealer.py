#Other libs
from random import randint
from config import *

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

        if((self._value < 2) or (self._value > 14)):
            rank = "Illegal rank"
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
        elif self._value == 14:
            rank = "A"
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
                newCard = Card(s, v + 2)
                self._cards.append(newCard)

    def printCards(self):
        """Print the cards of the entire deck (for testing)"""

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

    def dealHand(self, template = None):
        """Deal and display a hand from the deck"""

        hand = list()

        if(template is None):
            hand = self.dealCards()
        else:
            for ind in template:
                hand.append(self._deck.pop(ind))
                
        print("\nYour hand:")
        suits = -1  #Indicates that no card has been checked yet
        ladder = list()
        msg = ""

        for card in hand:
            card.printCard()
            ladder.append(card._value)

            #Check for flush
            if(suits < -1):
                continue
            elif(suits == -1):
                suits = card._suit
            elif(suits != card._suit):
                suits = -2 #Different suits

        #Check for pairs etc.
        ladder.sort(reverse = True)
        foot = 0
        head = len(ladder) - 1
        pattern = 0
        while(foot <= head):
            counter = ladder.count(ladder[foot])
            if counter == 1:
                ladder.append(ladder.pop(foot))
                head -= 1
            else:
                if counter == 4:
                    pattern = counter
                    foot += counter
                elif counter == 3:
                    if pattern == 2:
                        pattern = 32
                        ladder.append(ladder.pop(0))
                        ladder.append(ladder.pop(0))
                        foot += counter
                    else:
                        pattern = counter
                        foot += counter
                elif counter == 2:
                    if pattern == 3:
                        pattern = 32
                        foot += counter
                    elif pattern == 2:
                        pattern = 22
                        foot += counter
                    else:
                        pattern = counter
                        foot += counter
                else:
                    print("Illegal hand")
                    foot = head + 2

        #Check for straight
        if(pattern == 0):
            if(ladder[0] - ladder[4] == 4):
                pattern = ladder[0]
            elif(ladder[0] == 14 and ladder[1] == 5):
                pattern = ladder[1]

        if((pattern > 4) and (pattern <= 14)):
            msg = str(pattern) + "-high straight"
            if suits >= 0:
                msg += " flush"
        elif(suits >= 0):
            msg = str(ladder[0]) + "-high flush"
        elif(pattern == 4):
            msg = "quad " + str(ladder[0])
        elif(pattern == 32):
            msg = str(ladder[0]) + " full"
        elif(pattern == 3):
            msg = "trip " + str(ladder[0])
        elif(pattern == 22):
            msg = str(ladder[0]) + " up"
        elif(pattern == 2):
            msg = "a pair of " + str(ladder[0])
        else:
            msg = "high card " + str(ladder[0])

        print(msg)

    def dealCards(self, n = HAND_SIZE):
        """Deal and display cards from the deck."""

        hand = list()

        for i in range(n):
            hand.append(self._deck.pop(randint(0, len(self._deck) - 1)))
            #hand[i].printCard()

        return hand
