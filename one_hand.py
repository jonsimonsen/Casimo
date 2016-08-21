#Imports
from dealer import *

#initialise variables
cardRack = Dealer()

#main loop
cardRack.printCards()

for i in range(5):
    for j in range(5):
        cardRack.dealHand()
    cardRack.resetDeck()
