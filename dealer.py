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

        print("Shuffling cards...")     #For users of the simulation, it should be ok to assume that shuffling happens here.
        self._deck = list(self._cards)

    def readHand(self, hand):
        """Sorts the hand, prints what hand it is. Then returns the sorted hand."""

        cards = list(hand)      #cards to be sorted/classified
        foot = 0                #Index of the first unprocessed card
        head = len(hand) - 1    #Index of the last unprocessed card
        counter = 0             #To count the number of cards having the same rank as the card at foot
        pattern = 0             #Look in config.py for an overview of the possible patterns
        suits = -1              #-2 means that no flush is possible. -1 means that no card has been looked at. A positive number should correspond to the suit of the examined cards.

        #Sort, with aces first and deuces last
        cards.sort(key = lambda card: card._value, reverse = True)

        #Check for hands containing more than one card of equal rank (pairs, trips, two pair etc.)
        #The cards will be sorted so paired cards appear before unpaired and trips before pairs (in a full house)
        while(foot <= head):
            counter = sum(c._value == cards[foot]._value for c in cards)
            if counter == 1:
                #Move the card to the back. Move head forward, so the card will not be considered again.
                #Since all unpaired are treated this way, their order is preserved.
                cards.append(cards.pop(foot))
                head -= 1
            else:
                if counter == 4:
                    pattern = QUADS
                    foot = head + 1     #With quads at the foot, the hand is already sorted, so no need to loop again
                elif counter == 3:
                    if pattern == PAIR:
                        #A pair has already been processed. Since the trips are more interesting, the pair is moved to the end of the list
                        pattern = FULL_HOUSE
                        cards.append(cards.pop(0))
                        cards.append(cards.pop(0))
                        foot = head + 1     #With a full house, all cards have been sorted, so no need to loop again
                    else:
                        pattern = TRIPS
                        foot += counter     #The trips are in the right place. Move the foot to the first card that doesn't match their rank
                elif counter == 2:
                    if pattern == TRIPS:
                        #The trips have been processed, and the pair is therefore correctly placed
                        pattern = FULL_HOUSE
                        foot = head + 1     #With a full house, all cards have been sorted, so no need to loop again
                    elif pattern == PAIR:
                        #Since none of the pairs are moved, their order is preserved
                        pattern = TWO_PAIR
                        foot = head + 1     #With two pairs, the fifth card will always be in the correct place by now
                    else:
                        #The pair is likely to be correctly placed, so move the foot to the first card that doesn't match the rank
                        pattern = PAIR
                        foot += counter
                else:
                    #It is assumed that there are four suits and no jokers, so the count should never be outside the interval [1,4]
                    pattern = NO_HAND
                    foot = head + 1
                    print("Illegal hand")

        #If no cards were of equal rank, the hand is either a straigh flush, a flush, a straight or a hi-card hand.
        if(pattern == 0):
            #Check for straight, setting pattern to the highest card of the straight (5 is considered higher than A in 5-4-3-2-A)
            if(cards[0]._value - cards[4]._value == 4):
                pattern = cards[0]._value
            elif(cards[0]._value == 14 and cards[1]._value == 5):
                cards.append(cards.pop(0))
                pattern = cards[0]._value

            #Check for flush
            for card in cards:
                if(suits < -1):
                    continue
                elif(suits == -1):
                    suits = card._suit
                elif(suits != card._suit):
                    suits = -2 #Different suits

        self.printHandInfo(pattern, suits, cards[0])

    def printHandInfo(self, category, suits, firstcard):
        """Prints info about the hand based on its category, suitedness and most significant card"""

        msg = ""    #Message to be printed about the hand

        if(category < 0):
            #Illegal value
            msg = "Illegal value for the hand category."
        elif((category >= LOSTRAIGHT) and (category <= HISTRAIGHT)):
            #Straight or straight flush
            msg = firstcard.getValue() + "-high straight"
            if suits >= 0:
                msg += " flush."
            else:
                msg += "."
        elif(suits >= 0):
            msg = firstcard.getValue() + "-high flush."
        elif(category == QUADS):
            msg = "quad " + firstcard.getValue(-1) + "s."
        elif(category == FULL_HOUSE):
            msg = firstcard.getValue(-1) + "s full."
        elif(category == TRIPS):
            msg = "trip " + firstcard.getValue(-1) + "s."
        elif(category == TWO_PAIR):
            msg = firstcard.getValue(-1) + "s up."
        elif(category == PAIR):
            msg = "a pair of " + firstcard.getValue(-1) + "s."
        elif(category == HICARD):
            msg = "high card " + firstcard.getValue() + "."
        else:
            msg = "Unknown hand type."

        print(msg)

    def dealHand(self, template = None):
        """Deal and display a hand from the deck."""

        cards = list()

        #Deal a hand. The template argument can be used for testing.
        #It provides the possibility of a backdoor/cheat, so should probably be removed if used in a game.
        if(template is None):
            cards = self.dealCards()
        else:
            for ind in template:
                cards.append(self._deck.pop(ind))

        #Print the contents of the hand (can probably be removed after testing is complete)                
        print("\nYour hand:")
        
        for card in cards:
            card.printCard()

        #Sort the hand and display what kind of hand it is, then return it
        hand = self.readHand(cards)
        return hand

    def dealCards(self, n = HAND_SIZE):
        """Deal and display cards from the deck."""

        hand = list()

        for i in range(n):
            hand.append(self._deck.pop(randint(0, len(self._deck) - 1)))
            #hand[i].printCard()

        return hand
