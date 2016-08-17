#Other libs
from random import randint

#Global constants

MIN_STAKE = 4       #Number of chips for a big bet at the smallest stakes
MAX_STAKE = 8       #Number of chips for a big bet at the highest stakes
BUY_IN = 120        #Number of big bets required to sit down at a table
MAX_STACK = 240     #When posting the BB, this is the max amount of big bets allowed (must move up otherwise)
MIN_STACK = 60      #When posting the BB, this is the least amount of big bets allowed (must move down otherwise)
MIN_UNITS = 30      #When posting the BB at the lowest stakes, this is the least amount of big bets allowed (must leave otherwise)
MAX_TABLES = 10     #Maximum amount of tables at a stake
SEATS = 5           #Number of seats at a table

class Player(object):
    """A poker player"""

    def __init__(self, balance = MIN_STAKE * BUY_IN):
        """Setting up variables for the player"""

        self._chips = balance       #Default is based on having 480 small blinds at the smallest stakes (4)
        self._cash = 0              #Cash that is not converted to chips (if moving up, the remainder of cash that cannot be used to buy new chips end up here)
        self._played = 0            #Number of hands played
        self._status = 1            #0=seated, 1 = moving up (includes newly arrived players), 2 = moving down, 3 = busto
        self._ups = 0               #Number of times the player has moved up in stakes
        self._downs = 0             #Number of times the player has moved down in stakes

    def allin(self, stake = 4):
        """Bet the maximum amount on a hand. Used for testing. The finished simulator should be based on a limit structure."""

        self._chips -= stake * 6     #2 big bets predraw, 4 postdraw

class Table(object):
    """A poker table"""

    def __init__(self, stake = MIN_STAKE):
        """Setting up variables for the table"""

        self._stake = stake
        self._players = list()
        self._pot = 0       #Amount of chips in the middle
        self._button = 0    #The position of the button based on the index of the corresponding player
        self._rounds = 0

    def seat(self, player, position = -1):
        """Seat a player at the table"""

        if position < 0:
            pos = (self._button + 2) % 5
        else:
            pos = position

        player._status = 0 #seated
        self._players.insert(pos, player)

    def playHand(self):
        """Play one hand at the table"""

        for player in self._players:
            player.allin(self._stake)
            player._played += 1
            self._pot += 6 * MIN_STAKE

        #Award the pot to a random player
        self._players[randint(0, 4)]._chips += self._pot
        self._pot = 0
        
        #Move button
        self._button = (self._button + 1) % 5
        self._rounds += 1

        #Move the new big blind up or down if required
        bb = (self._button + 2) % 5
        if(self._players[bb]._chips >= self._stake * MAX_STACK):
            self._players[bb]._status = 1
            return self._players.pop(bb)
        elif((self._stake > MIN_STAKE) and (self._players[bb]._chips <= self._stake * MIN_STACK)):
            self._players[bb]._status = 2
            return self._players.pop(bb)
        elif((self._stake <= MIN_STAKE) and (self._players[bb]._chips <= self._stake * MIN_UNITS)):
            self._players[bb]._status = 3
            return self._players.pop(bb)
        else:
            return None

    def reportStacks(self):
        """Report the stack sizes for the players"""
        for i in range(len(self._players)):
            output = "\tSeat #" + str(i) + ": " + str(self._players[i]._chips) + " chips"
            print(output)

        print("")

class Manager(object):
    """A stake manager (responsible for all tables having a certain stake)"""

    def __init__(self, stake = MIN_STAKE, tables = MAX_TABLES, cashier = None):
        """Setting up variables for the manager"""

        self._stake = stake
        self._numtables = tables
        self._cashier = cashier
        self._tables = list()
        self._freeTables = list()   #Tables that are not filled
        self._waitList = list()
        self._rounds = 0
        self._boss = None   #When higher stakes exist, this should be the Manager at the next stakes
        self._upList = list()
        self._downList = list()

    def fillWaitList(self):
        """Fills the waitlist with players for one table (populating the waitlist will be implemented differently later)"""
        for i in range(SEATS):
            newFace = Player()
            self._waitList.append(newFace)

    def startTables(self):
        """Start new tables, populating them with players from the waitList. This process repeats until there are not enough player left in the waitList for another full table."""

        while((len(self._tables) < MAX_TABLES) and (len(self._waitList) > SEATS)):
            newTab = Table(self._stake)

            for i in range(SEATS):
                newTab.seat(self._waitList.pop(0), i)

            self._tables.append(newTab)

    def startHand(self):
        """Starts a new hand at all tables"""

        #Get a list of players moving down to the manager's stakes from his boss
        if self._boss is not None:
            for mover in self._boss._downList:
                self._cashier.handleMover(mover, self._boss._stake, self._stake)
                self._waitList.append(mover)

            self._boss.downList = list()

        #Fill tables from the waitList
        for i in range(len(self._waitList)):
            if(len(self._freeTables) > 0):
                self._freeTables[0].seat(self._waitList.pop(0))
                self._tables.append(self._freeTables.pop(0))
            else:
                break

        #Make new tables for the remaining players in the waitlist
        self.startTables()
        
        for table in self._tables:
            mover = table.playHand()

            if mover is not None:
                self._tables.remove(table)
                self._freeTables.append(table)

                if(mover._status == 3):
                    self._cashier.handleBust(mover)
                elif(mover._status == 2):
                    mover._ups += 1
                    self._upList.append(mover)
                elif(mover._status == 1):
                    self._downList.append(mover)
                    mover._downs += 1

        self._rounds += 1

        if(self._stake == MAX_STAKE):
            for winner in self._upList:
                self._cashier.handleBreak(winner)
        elif(len(self._upList) > 0):
            if(self._boss is None):
                self.hireBoss()     #Not a natural way of hiring. Since the simulator doesn't care about human relationships, it seems ok

            for mover in self._upList:
                self._cashier.handleMover(mover, self._stake, self._boss._stake)
                self._boss.waitList.append(mover)

        self._upList = list()   #All move ups have been handled, so reset the list

    def hireBoss(self):
        """When there is noone responsible for the next level of stakes, a boss is hired for the manager"""

        newMan = Manager(self._stake * 2, cashier = self._cashier)  #TODO: Look into scaling down the number of tables at higher stakes
        self._boss = newMan

    def makeReport(self):
        """Report the stack sizes at the tables"""

        for i in range(len(self._tables)):
            header = "Table #" + str(i) +"\n"
            print(header)
            self._tables[i].reportStacks()

        for j in range(len(self._freeTables)):
            header = "Table #" + str(j) +"\n"
            print(header)
            self._freeTables[j].reportStacks()            

class Cashier(object):
    """A cashier that gives players back cash based on their amount of chips"""

    def __init__(self):
        """Setting up variables for the cashier"""

        self._bustos = list()       #Keeps track of the players that leaves and the amount of cash they take with them
        self._highRollers = list()  #Keeps track of the players that are waiting for higher stakes, and their amount of cash they have

    def handleBust(self, busto, stake = MIN_STAKE):
        """Handles a player that has too few chips to keep playing"""

        busto._cash += busto._chips * stake / MIN_STAKE
        busto._chips = 0

        #Keep track of the player
        self._bustos.append(busto)

    def handleBreak(self, winner, stake = MAX_STAKE):
        """Handle a player that has too many chips to keep playing at the simulated tables"""

        winner._cash += winner._chips * stake / MIN_STAKE
        winner._chips = 0

        #Keep track of the player
        self._highRollers.append(winner)

    def handleMover(self, mover, oldstake, newstake):
        """Handle a player that is about to move up or down"""

        mover._cash += winner._chips * oldstake / MIN_STAKE
        mover._chips = mover._cash // newstake
        mover._cash %= newstake

    def makeReport(self):
        """Report on the players that have left the casino"""

        print("Cash of highrollers:")
        for winner in self._highRollers:
            print("\t" + str(winner._cash))

        print("Cash of bustos:")
        for busto in self._bustos:
            print("\t" + str(busto._cash))
