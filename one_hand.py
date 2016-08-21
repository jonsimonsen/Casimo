#Imports
from dealer import *

#initialise variables
cardRack = Dealer()

#main loop
#cardRack.printCards()

for test in TESTIN:
    cardRack.dealHand(test)
    cardRack.resetDeck()
"""for i in range(5):
    for j in range(5):
        cardRack.dealHand()
    cardRack.resetDeck()"""
