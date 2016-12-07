#Imports
from entities import *
from conftest import *

#Initialise variables
cardRack = Dealer()

#test cases

print('\nSorted:\n')

for subgroup in TSORT:
    for case in subgroup:
        cardRack._createHand(case)

print('\nUnsorted:\n')

for unsubgroup in TUNSORT:
    for uncase in unsubgroup:
        cardRack._createHand(uncase)
