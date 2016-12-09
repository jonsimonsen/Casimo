#Imports
from entities import *
from conftest import *

#Initialise variables
cardRack = Dealer()
callStation = Player()

#test cases

print('\nSorted:\n')

for subgroup in TSORT:
    for case in subgroup:
        cardRack._createHand(case)

print('\nUnsorted:\n')

for unsubgroup in TUNSORT:
    for uncase in unsubgroup:
        cardRack._createHand(uncase)

print('\nPair and draw:\n')

for pdgroup in TPSORT:
    for pdcase in pdgroup:
        callStation.setHand(cardRack._createHand(pdcase))

print('\nFake draws:\n')

for fakes in FSTRFL:
    callStation.setHand(cardRack._createHand(fakes))

print('\nDrawing hands:\n')

for dgroup in TDSORT:
    for dcase in dgroup:
        callStation.setHand(cardRack._createHand(dcase))
