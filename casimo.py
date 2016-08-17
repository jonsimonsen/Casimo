#Imports
from entities import *

#Global constants
HANDS_PER_ROUND = 10    #Number of hands played in each round (per table)
ROUNDS = 10             #Number of rounds to run the simulator

#initialising variables
moneyBags = Cashier()
boss = Manager(cashier = moneyBags)

#Initialise the maximum amount of tables for the manager
for i in range(MAX_TABLES):
    boss.fillWaitList()

#main loop (for now testing ten rounds, presumably at a single table)

for i in range(ROUNDS):
    for j in range(HANDS_PER_ROUND):
        boss.startHand()
    boss.makeReport()
    moneyBags.makeReport()
