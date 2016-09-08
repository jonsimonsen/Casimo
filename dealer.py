#Imports/libs
from random import randint
from config import *

class Card(object):
    """A playing card. Has a suit and a value with ranges that should be defined in config.py"""

    #At a later stage, it might be convenient to be able to display symbols for suits
    #and shorter description for ranks.

    def __init__(self, suit, value):
        """Create a card with the given suit and rank. Raises a ValueError if any of the arguments are invalid."""

        #Make sure that the given parameters are valid
        if(suit in SUITS):
            self._suit = suit
        else:
            raise ValueError("suit must correspond to a member of SUITS in config.py")
        if value >= MIN_RANK and value <= MAX_RANK:
            self._value = value
        else:
            raise ValueError("value must be between MIN_RANK and MAX_RANK in config.py")

    def getSuit(self):
        """Getter for _suit"""
        return self._suit

    def getValue(self):
        """Getter for _value"""
        return self._value

    def strSuit(self):
        """Return a string corresponding to the suit of the card."""

        if self._suit == CLUBS:
            return "clubs"
        elif self._suit == DIAMONDS:
            return "diamonds"
        elif self._suit == HEARTS:
            return "hearts"
        elif self._suit == SPADES:
            return "spades"
        else:
            return "illegal suit"

    def strValue(self, context = 0):
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
        else:
            return "illegal rank"

    def printCard(self):
        """Print info about the card (rank and suit)."""

        print("\t" + self.strValue() + " of " + self.strSuit())

class PokerPerson(object):
    """An adt class for persons sitting at a poker table (players and dealer)."""

    def __init(self):
        """Default initialization of the ADT."""

        print("Please don't try to initialize an object of this ADT.")

    def readHand(self, hand):
        """Default method for reading and classifying a poker hand."""

        print("Please make sure to implement a readHand method for the descendant of this ADT.")

class Dealer(PokerPerson):
    """A poker dealer.

    _cards: A full deck of cards that should be immutable.
    _deck: An actual deck of cards that can be used(mutated).

    It seems unnecessary to actually shuffle the cards at the start of a new round, so the dealer should just
    pick (pop) a random card from the deck for each dealt card.
    Since the deck will no longer contain the cards that was drawn during the latest round, a
    resetDeck() method can be called to reassemble the deck.
    """

    def __init__(self):
        """Create a dealer with a dummy version of a deck (that can't be altered), and an actual deck."""

        #Set up a full deck that can be copied into an actual deck when starting a new hand
        #This seemed easier than collecting cards from the muck before a new deal.
        self._cards = list()
        self._initCards()

        #Initialize the actual deck
        self._deck = list()
        self.resetDeck()

    def _initCards(self):
        """Create the cards of a deck. Only planned use is for the constructor."""

        for s in SUITS:
            for v in range(MIN_RANK, MAX_RANK + 1):
                newCard = Card(s, v)
                self._cards.append(newCard)

    def resetDeck(self):
        """Reassemble the deck by making _deck a copy of _cards."""

        #Copy the dummy deck     
        self._deck = list(self._cards)

    def dealHand(self):
        """Deal and display a hand from the deck."""

        cards = list()

        #Deal a hand.
        cards = self.dealCards()

        #Sort the hand and display what kind of hand it is, then return it
        hand = self.readHand(cards)
        return hand

    def dealCards(self, n = HAND_SIZE):
        """Deal a given number of cards from the deck.

        n: Number of cards to deal.

        returns a list containing the dealt cards.
"""

        hand = list()

        for i in range(n):
            hand.append(self._deck.pop(randint(0, len(self._deck) - 1)))

        return hand

    def readHand(self, hand):
        """Sorts the hand. Prints what hand it is. Then returns the sorted hand."""

        cards = list(hand)      #cards to be sorted/classified
        foot = 0                #Index of the first unprocessed card
        head = len(cards) - 1   #Index of the last unprocessed card
        counter = 0             #To count the number of cards having the same rank as the card at foot
        pattern = 0             #Look in config.py for an overview of the possible patterns

        #Sort, with aces first and deuces last
        cards.sort(key = lambda card: card._value, reverse = True)

        #Check for hands containing more than one card of equal rank (pairs, trips, two pair etc.)
        #The cards will be sorted so paired cards appear before unpaired and trips before pairs (in a full house)
        while(foot <= head):
            counter = sum(c.getValue() == cards[foot].getValue() for c in cards)
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
            #Order a wheel (5-high straight) correctly
            if cards[0].getValue() == 14 and cards[1].getValue() == 5:
                cards.append(cards.pop(0))
                
            #Check for straights and flushes
            pattern = self.findSequence(cards)
 
        self.printHandInfo(pattern, cards[0])
        return cards
    
    def showDown(self, players, potsize):
        """Awards the pot to the player with the best hand."""

        bestHand = self.dealHand(NUTLOW)
        cmpVal = 0
        winners = list()

        for player in players:
            hand = player.getHand()
            cmpVal = self.cmpHands(hand, bestHand)

            if cmpVal > 0:
                winners = list()    #Remove beaten players from the list
                winners.append(player)
                bestHand = hand
            elif cmpVal == 0:
                winners.append(player)

        #print("winners: " + str(len(winners)) + "\n")
        
        winnings = potsize // len(winners)
        rest = potsize % len(winners)

        while rest != 0:
            winners[randint(0, len(winners) - 1)].chipUp(1)
            rest -= 1

        for winner in winners:
            winner.chipUp(winnings)

    def cmpHands(self, firstHand, lastHand):
        """Return 1 if the first hand is best, 0 if they're equal and -1 otherwise."""

        first = self.rateHand(firstHand)
        last = self.rateHand(lastHand)

        if first > last:
            return 1
        elif first < last:
            return -1
        else:
            for i in range(len(firstHand)):
                if firstHand[i].getValue() > lastHand[i].getValue():
                    return 1
                elif firstHand[i].getValue() < lastHand[i].getValue():
                    return -1

            return 0

    def rateHand(self, hand):
        """Returns a number telling what category the hand belongs in"""

        counter = sum(card.getValue() == hand[0].getValue() for card in hand)

        if counter == 4:
            return QUADS
        elif counter == 3:
            if hand[3].getValue() == hand[4].getValue():
                return FULL_HOUSE
            else:
                return TRIPS
        elif counter == 2:
            if hand[2].getValue() == hand[3].getValue():
                return TWO_PAIR
            else:
                return PAIR
        elif counter != 1:
            return NO_HAND
        else:
            return self.findSequence(hand)
 
    def findSequence(self, hand):
        """Returns the pattern found (straight, flush, straightflush or hicard). It is assumed that the caller has already verified that there are no duplicated ranks in the hand."""

        suitCount = sum(card.getSuit() == hand[0].getSuit() for card in hand) #Number of cards having the same suit as the first card
        if(hand[0].getValue() == 5) or (hand[0].getValue() - hand[4].getValue() == 4):
            if suitCount == 5:
                return STRFL
            else:
                return STRAIGHT
        elif suitCount == 5:
            return FLUSH
        else:
            return HICARD
        
    def _printCards(self):
        """Print the cards of the entire deck (for testing)"""

        for card in self._cards:
            card.printCard()

    def printDeck(self):
        """Print the cards left in the actual deck"""

        for card in self._deck:
            card.printCard()

    def printHandInfo(self, category, firstcard):
        """Prints info about the hand based on its category, suitedness and most significant card"""

        msg = ""    #Message to be printed about the hand

        if category < 0:
            #Illegal value
            msg = "Illegal value for the hand category."
        elif category == HICARD:
            msg = "high card " + firstcard.strValue() + "."
        elif category == PAIR:
            msg = "a pair of " + firstcard.strValue(-1) + "s."
        elif category == TWO_PAIR:
            msg = firstcard.strValue(-1) + "s up."
        elif category == TRIPS:
            msg = "trip " + firstcard.strValue(-1) + "s."
        elif category == STRAIGHT:
            msg = firstcard.strValue() + "-high straight."
        elif category == FLUSH:
            msg = firstcard.strValue() + "-high flush."
        elif category == FULL_HOUSE:
            msg = firstcard.strValue(-1) + "s full."
        elif category == QUADS:
            msg = "quad " + firstcard.strValue(-1) + "s."
        elif category == STRFL:
            msg = firstcard.strValue() + "-high straight flush."
        else:
            msg = "Unknown hand type."

        print(msg)

    def _createHand(self, template):
        """Method that creates specific hands. Details omitted to avoid unauthorized use."""

        #Deal a hand.
        #The template argument should contain a list of indices corresponding to the position of the cards in a newly reset deck.
        #It is easiest to sort the list descending, since popping messes with the indices of the following elements.
        #The method provides the possibility of a backdoor/cheat, so should probably be removed if used in a game.

        cards = list()

        #Reset the deck to make sure that the intended cards are drawn
        self.resetDeck()
            
        for ind in template:
            cards.append(self._deck.pop(ind))

        #Sort the hand and display what kind of hand it is. The return it.
        hand = self.readHand(cards)
        return hand
