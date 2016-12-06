#Imports
from entities import *
from conftest import *

#Initialise variables
cardRack = Dealer()

#main loop

for subgroup in TSORT:
    for case in subgroup:
        cardRack._createHand(case)
