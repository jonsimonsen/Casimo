#Imports/libs
from random import randint
from config import *

class Card(object):
    """A playing card"""

    def __init__(self, suit, value):
        """Setting up variables for the card"""

        self._suit = suit
        self._value = value

    def printCard(self):
        """Print info about the card (rank and suit)"""

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

    def getValue(self, context = 0):
        """Return a string corresponding to the rank of the card."""

        if(self._value == 2):
            return "deuce"
        elif(self._value == 3):
            return "trey"
        elif(self._value == 4):
            return "four"
        elif(self._value == 5):
            return "five"
        elif(self._value == 6):
            if context == 0:
                return "six"
            else:
                return "sixe" #hack to get the correct plural
        elif(self._value == 7):
            return "seven"
        elif(self._value == 8):
            return "eight"
        elif(self._value == 9):
            return "nine"
        elif(self._value == 10):
            return "ten"
        elif(self._value == 11):
            return "jack"
        elif(self._value == 12):
            return "queen"
        elif(self._value == 13):
            return "king"
        elif(self._value == 14):
            return "ace" 

class Dealer(object):
    """A poker dealer"""

    def __init__(self):
        """Setting up variables for the dealer"""

        #Set up a full deck that can be copied into an actual deck when starting a new hand
        #This seemed easier than collecting cards from the muck before a new deal.
        self._cards = list()
        self.getCards()

        #Initialize the actual deck
        self._deck = list()
        self.resetDeck()

    def getCards(self):
        """Initialize the cards of a deck"""

        for s in range(SUITS):
            for v in range(VALUES):
                newCard = Card(s, v + 2) #Add 2, since it's convenient that values range from 2 (deuces) to 14 (aces).
                self._cards.append(newCard)

    def printCards(self):
        """Print the cards of the entire deck (for testing)"""

        for card in self._cards:
            card.printCard()

    def printDeck(self):
        """Print the cards left in the actual deck"""

        for card in self._deck:
            card.printCard()

    def resetDeck(self):
        """Make _deck a copy of _cards"""

        print("Shuffling cards...")
        self._deck = list(self._cards)

    def dealHand(self, template = None):
        """Deal and display a hand from the deck."""

        hand = list()

        #Deal a hand. The template argument can be used for testing.
        #It provides the possibility of a backdoor/cheat, so should probably be removed if used in a game.
        if(template is None):
            hand = self.dealCards()
        else:
            for ind in template:
                hand.append(self._deck.pop(ind))
                
        print("\nYour hand:")
        
        suits = -1  #Indicates that no card has been checked yet
        msg = ""

        for card in hand:
            card.printCard()

            #Check for flush
            if(suits < -1):
                continue
            elif(suits == -1):
                suits = card._suit
            elif(suits != card._suit):
                suits = -2 #Different suits

        #Check for pairs etc.
        hand.sort(key = lambda card: card._value, reverse = True)
        foot = 0
        head = len(hand) - 1
        pattern = 0
        while(foot <= head):
            counter = sum(c._value == hand[foot]._value for c in hand)
            if counter == 1:
                hand.append(hand.pop(foot))
                head -= 1
            else:
                if counter == 4:
                    pattern = counter
                    foot += counter
                elif counter == 3:
                    if pattern == 2:
                        pattern = 32
                        hand.append(hand.pop(0))
                        hand.append(hand.pop(0))
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
            if(hand[0]._value - hand[4]._value == 4):
                pattern = hand[0]._value
            elif(hand[0]._value == 14 and hand[1]._value == 5):
                hand.append(hand.pop(0))
                pattern = hand[0]._value

        if((pattern > 4) and (pattern <= 14)):
            msg = hand[0].getValue() + "-high straight"
            if suits >= 0:
                msg += " flush."
            else:
                msg += "."
        elif(suits >= 0):
            msg = hand[0].getValue() + "-high flush."
        elif(pattern == 4):
            msg = "quad " + hand[0].getValue(-1) + "s."
        elif(pattern == 32):
            msg = hand[0].getValue(-1) + "s full."
        elif(pattern == 3):
            msg = "trip " + hand[0].getValue(-1) + "s."
        elif(pattern == 22):
            msg = hand[0].getValue(-1) + "s up."
        elif(pattern == 2):
            msg = "a pair of " + hand[0].getValue(-1) + "s."
        else:
            msg = "high card " + hand[0].getValue() + "."

        print(msg)

        for card in hand:
            card.printCard()

        print("")

    def dealCards(self, n = HAND_SIZE):
        """Deal and display cards from the deck."""

        hand = list()

        for i in range(n):
            hand.append(self._deck.pop(randint(0, len(self._deck) - 1)))
            #hand[i].printCard()

        return hand
