#Imports
from entities import *

#Global constants
ROUNDS = 10     #Number of rounds to run the simulator

#initialising variables
boss = Manager()
boss.fillWaitList()
boss.startTable()

#main loop (for now testing ten rounds, presumably at a single table)

for i in range(ROUNDS):
    boss.startHand()
    boss.makeReport()

