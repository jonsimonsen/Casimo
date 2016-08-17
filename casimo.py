#Imports
from entities import *

#Global constants
ROUNDS = 10     #Number of rounds to run the simulator

#initialising variables
moneyBags = Cashier()
boss = Manager(cashier = moneyBags)

#Initialise the maximum amount of tables for the manager
for i in range(MAX_TABLES):
    boss.fillWaitList()
    boss.startTable()

#main loop (for now testing ten rounds, presumably at a single table)

while(len(boss._tables) > 0):
    boss.startHand()

#Make reports on the status
boss.makeReport()
moneyBags.makeReport()

"""for i in range(ROUNDS):
    boss.startHand()
    boss.makeReport()"""
