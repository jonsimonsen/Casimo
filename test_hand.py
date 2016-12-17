#Imports
from entities import *
from conftest import *

#Initialise variables
cardRack = Dealer()
callStation = Player()

#test cases

print('Sorted')
print('------\n')

for subgroup in TSORT:
    for case in subgroup:
        if isinstance(case, str):
            print(case)
        else:
            cardRack._createHand(case)
        print('')

print('Unsorted')
print('--------\n')

for unsubgroup in TUNSORT:
    for uncase in unsubgroup:
        if isinstance(uncase, str):
            print(uncase)
        else:
            cardRack._createHand(uncase)
        print('')

print('Pair and draw')
print('-------------\n')

for pdgroup in TPSORT:
    for pdcase in pdgroup:
        if isinstance(pdcase, str):
            print(pdcase)
        else:
            callStation.setHand(cardRack._createHand(pdcase))
        print('')

print('Fake draws')
print('----------\n')

for fake in FSTRFL:
    if isinstance(fake, str):
        print(fake)
    else:
        callStation.setHand(cardRack._createHand(fake))
    print('')

print('Drawing hands')
print('-------------\n')

for dgroup in TDSORT:
    for dcase in dgroup:
        if isinstance(dcase, str):
            print(dcase)
        else:
            callStation.setHand(cardRack._createHand(dcase))
        print('')
