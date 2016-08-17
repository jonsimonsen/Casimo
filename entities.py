#Other libs
from random import randint

#Global constants

MIN_STAKE = 4       #Number of chips for a big bet at the smallest stakes
BUY_IN = 120        #Number of big bets required to sit down at a table
MAX_STACK = 240     #When posting the BB, this is the max amount of big bets allowed (must move up otherwise)
MIN_STACK = 60      #When posting the BB, this is the least amount of big bets allowed (must move down otherwise)
MIN_UNITS = 30      #When posting the BB at the lowest stakes, this is the least amount of big bets allowed (must leave otherwise)
MAX_TABLES = 10      #Maximum amount of tables at a stake
SEATS = 5           #Number of seats at a table

class Player(object):
    """A poker player"""

    def __init__(self, balance = MIN_STAKE * BUY_IN):
        """Setting up variables for the player"""

        self._chips = balance       #Default is based on having 480 small blinds at the smallest stakes (4)
        self._cash = 0              #Cash that is not converted to chips (if moving up, the remainder of cash that cannot be used to buy new chips end up here)
        self._played = 0            #Number of hands played

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

        #Return busted player (if any)
        bb = (self._button + 2) % 5
        if(self._players[bb]._chips < MIN_STAKE * MIN_UNITS):
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

    def fillWaitList(self):
        """Fills the waitlist with five players (populating the waitlist will be implemented differently later)"""
        for i in range(5):
            newFace = Player()
            self._waitList.append(newFace)

    def startTable(self):
        """Starts a new table, populating it with players from the waitList."""

        if len(self._tables) < self._numtables:
            newTab = Table(self._stake)
            for i in range(5):
                newTab.seat(self._waitList.pop(0), i)
                
            self._tables.append(newTab)

    def startHand(self):
        """Starts a new hand at all tables"""
        
        for table in self._tables:
            busto = table.playHand()

            if busto is not None:
                self._tables.remove(table)
                self._freeTables.append(table)
                self._cashier.handleBust(busto)

        self._rounds += 1

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

        self._bustos = list()   #Keeps track of the players that leaves and the amount of cash they take with them

    def handleBust(self, busto, stake = MIN_STAKE):
        """Handles a player that has too few chips to keep playing"""

        busto._cash += busto._chips * stake / MIN_STAKE
        busto._chips = 0

        #Keep track of the player
        self._bustos.append(busto)

    def makeReport(self):
        """Report on the players that have left the casino"""

        print("Cash of bustos:")
        for busto in self._bustos:
            print("\t" + str(busto._cash))
