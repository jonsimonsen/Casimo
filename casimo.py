#Imports
from entities import *
from loose import *
from regular import *
from tight import *

#Global constants
HANDS_PER_ROUND = 100   #Number of hands played in each round (per table)
ROUNDS = 10             #Number of rounds to run the simulator

#initialising variables
playerTypes = [LOOSE, REGULAR, TIGHT]
moneyBags = Cashier()
sheepDog = Recruiter(playerTypes)
cardRack = Dealer()
boss = Manager(cashier = moneyBags, recruiter = sheepDog, dealer = cardRack)

#Initialize the waitList with enough players for one table
boss.fetchPlayers(SEATS)

#main loop (for now testing ten rounds, presumably at a single table)

for i in range(ROUNDS):
    for j in range(HANDS_PER_ROUND):
        boss.startHand()
    boss.makeReport()
    
moneyBags.makeReport()
