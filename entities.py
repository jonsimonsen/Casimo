#Other libs
from random import *

#Global constants

MIN_STAKE = 4       #Number of chips for a big bet at the smallest stakes
BUY_IN = 120        #Number of big bets required to sit down at a table
MAX_STACK = 240     #When posting the BB, this is the max amount of big bets allowed (must move up otherwise)
MIN_STACK = 60      #When posting the BB, this is the least amount of big bets allowed (must move down otherwise)
MIN_UNITS = 30      #When posting the BB at the lowest stakes, this is the least amount of big bets allowed (must leave otherwise)
MAX_TABLES = 1      #Maximum amount of tables at a stake
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
        #When implementing sensible players, the button should also move

        #Not implementing busting/moving up or down yet

        self._rounds += 1

    def reportStacks(self):
        """Report the stack sizes for the players"""
        for i in range(len(self._players)):
            output = "\tSeat #" + str(i) + ": " + str(self._players[i]._chips) + " chips"
            print(output)

        print("")

class Manager(object):
    """A stake manager (responsible for all tables having a certain stake)"""

    def __init__(self, stake = MIN_STAKE, tables = MAX_TABLES):
        """Setting up variables for the manager"""

        self._stake = stake
        self._numtables = tables
        self._tables = list()
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
            table.playHand()

        self._rounds += 1

    def makeReport(self):
        """Report the stack sizes at the tables"""

        for i in range(len(self._tables)):
            header = "Table #" + str(i) +"\n"
            print(header)
            self._tables[i].reportStacks()
