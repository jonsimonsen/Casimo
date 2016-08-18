#Imports
from entities import *

#Global constants
HANDS_PER_ROUND = 20    #Number of hands played in each round (per table)
ROUNDS = 10             #Number of rounds to run the simulator

#initialising variables
moneyBags = Cashier()
sheepDog = Recruiter()
boss = Manager(cashier = moneyBags, recruiter = sheepDog)

#Initialize the waitList with enough players for one table
boss.getPlayers(SEATS)

#main loop (for now testing ten rounds, presumably at a single table)

for i in range(ROUNDS):
    for j in range(HANDS_PER_ROUND):
        boss.startHand()
    boss.makeReport()
    moneyBags.makeReport()
