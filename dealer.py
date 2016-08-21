#Global constants
SUITS = 4
VALUES = 13

#Classes

class Card(object):
    """A playing card"""

    def __init__(self, suit, value):
        """Setting up variables for the card"""

        self._suit = suit
        self._value = value

class Dealer(object):
    """A poker dealer"""

    def __init__(self):
        """Setting up variables for the dealer"""

        self._cards = list()
        self.getCards()

    def getCards(self):
        """Initialize the cards with the 52 cards of a deck"""

        for s in range(SUITS):
            for v in range(VALUES):
                newCard = Card(s, v + 1)
                self._cards.append(newCard)

    def printCards(self):
        """Print the cards of the sorted deck"""

        rank = ""
        color = ""
        res = ""

        for card in self._cards:
            if card._value == 1:
                rank = "A"
            elif card._value < 10:
                rank = str(card._value)
            elif card._value == 10:
                rank = "T"
            elif card._value == 11:
                rank = "J"
            elif card._value == 12:
                rank = "Q"
            elif card._value == 13:
                rank = "K"
            else:
                rank = "Illegal rank"

            if card._suit == 0:
                color = "clubs"
            elif card._suit == 1:
                color = "diamonds"
            elif card._suit == 2:
                color = "hearts"
            elif card._suit == 3:
                color = "spades"
            else:
                color = "illegal suit"

            print(rank + " of " + color)
