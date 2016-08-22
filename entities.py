#Other libs
from random import randint
from dealer import * #Includes global constants

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

    def allin(self):
        """Bet the maximum amount on a hand. Used for testing. The finished simulator should be based on a limit structure."""

        self._chips -= MIN_STAKE * 6     #2 big bets predraw, 4 postdraw

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
            player.allin()
            player._played += 1
            self._pot += 6 * MIN_STAKE

        #Award the pot to a random player
        self._players[randint(0, SEATS - 1)]._chips += self._pot
        self._pot = 0

        #Return the player from the big blind if that player can no longer play at these stakes
        mover = self.finishHand()
        return mover

    def finishHand(self):
        """Do cleanup after the hand has finished"""

        #Move button
        self._button = (self._button + 1) % 5
        self._rounds += 1

        #Move the new big blind up or down if required
        bb = (self._button + 2) % 5
        if(self._players[bb]._chips >= MIN_STAKE * MAX_STACK):
            self._players[bb]._status = 1
            return self._players.pop(bb)
        elif((self._stake > MIN_STAKE) and (self._players[bb]._chips <= MIN_STAKE * MIN_STACK)):
            self._players[bb]._status = 2
            return self._players.pop(bb)
        elif((self._stake <= MIN_STAKE) and (self._players[bb]._chips < MIN_STAKE * MIN_UNITS)):
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

    def __init__(self, stake = MIN_STAKE, tables = MAX_TABLES, cashier = None, recruiter = None):
        """Setting up variables for the manager"""

        self._stake = stake
        self._numtables = tables
        self._cashier = cashier
        self._recruiter = recruiter
        self._tables = list()
        self._freeTables = list()   #Tables that are not filled
        self._waitList = list()     #Players waiting to be seated at the manager's stakes
        self._rounds = 0            #Rounds played globally since the manager was hired (even if no tables at these stakes played a hand in the round)
        self._boss = None           #When higher stakes exist, this should be the Manager at the next stakes
        self._upList = list()       #People that were playing here, and should now be transferred to a waiting list at higher stakes
        self._downList = list()     #People that were playing here, and should now be transferred to a waiting list at lower stakes

    def getPlayers(self, n = 1):
        """Fills the waitlist with n players"""
        
        self._waitList.extend(self._recruiter.findPlayers(n))

    def startTables(self):
        """Start new tables, populating them with players from the waitList. This process repeats until there are not enough player left in the waitList for another full table."""

        while((len(self._tables) < self._numtables) and (len(self._waitList) >= SEATS)):
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

            self._boss._downList = list()

        #If there are too many empty tables, ask the recruiter to find a new player
        if(self._recruiter is not None):
            if((len(self._tables) + len(self._freeTables) < self._numtables) or (len(self._freeTables) > len(self._waitList))):
                self.getPlayers()

        #Fill tables from the waitList
        for i in range(len(self._waitList)):
            if(len(self._freeTables) > 0):
                self._tables.append(self._freeTables.pop(0))
                self._tables[-1].seat(self._waitList.pop(0))
            else:
                break

        #Make new tables for the remaining players in the waitlist
        self.startTables()

        #Play a hand at each table. Handle moving players between stakes
        for table in self._tables:
            mover = table.playHand()

            if mover is not None:
                self._tables.remove(table)
                self._freeTables.append(table)

                if(mover._status == 3):
                    self._cashier.handleBust(mover)
                elif(mover._status == 2):
                    mover._downs += 1
                    self._downList.append(mover)
                elif(mover._status == 1):
                    self._upList.append(mover)
                    mover._ups += 1
                else:
                    print("Error: Illegal status on a player.")

        self._rounds += 1

        if(self._stake == MAX_STAKE):
            for winner in self._upList:
                self._cashier.handleBreak(winner)
        elif(len(self._upList) > 0):
            if(self._boss is None):
                self.hireBoss()     #Not a natural way of hiring. Since the simulator doesn't care about human relationships, it seems ok

            for mover in self._upList:
                self._cashier.handleMover(mover, self._stake, self._boss._stake)
                self._boss._waitList.append(mover)

        self._upList = list()   #All move ups have been handled, so reset the list

        #Start a new hand at the next level of stakes
        if self._boss is not None:
            self._boss.startHand()

    def hireBoss(self):
        """When there is noone responsible for the next level of stakes, a boss is hired for the manager"""

        newMan = Manager(self._stake * 2, cashier = self._cashier)  #TODO: Look into scaling down the number of tables at higher stakes
        self._boss = newMan

    def makeReport(self):
        """Report the stack sizes at the tables"""

        mainhead = "Report for " + str(self._stake) + " unit stakes after " + str(self._rounds) + " hands played.\n"
        print(mainhead)
        
        for i in range(len(self._tables)):
            header = "Table #" + str(i) + " after " + str(self._tables[i]._rounds) + " hands.\n"
            print(header)
            self._tables[i].reportStacks()

        for j in range(len(self._freeTables)):
            header = "Table #" + str(len(self._tables) + j) + " after " + str(self._freeTables[j]._rounds) + " hands.\n"
            print(header)
            self._freeTables[j].reportStacks()


        if(self._boss is not None):
            self._boss.makeReport()

class Cashier(object):
    """A cashier that gives players back cash based on their amount of chips"""

    def __init__(self):
        """Setting up variables for the cashier"""

        self._bustos = list()       #Keeps track of the players that leaves and the amount of cash they take with them
        self._highRollers = list()  #Keeps track of the players that are waiting for higher stakes, and their amount of cash they have

    def handleBust(self, busto, stake = MIN_STAKE):
        """Handles a player that has too few chips to keep playing"""

        busto._cash += busto._chips * stake // MIN_STAKE
        busto._chips = 0

        #Keep track of the player
        self._bustos.append(busto)

    def handleBreak(self, winner, stake = MAX_STAKE):
        """Handle a player that has too many chips to keep playing at the simulated tables"""

        winner._cash += winner._chips * stake // MIN_STAKE
        winner._chips = 0

        #Keep track of the player
        self._highRollers.append(winner)

    def handleMover(self, mover, oldstake, newstake):
        """Handle a player that is about to move up or down"""

        #print("Before:")
        #print(str(mover._chips))
        mover._cash += mover._chips * oldstake // MIN_STAKE
        mover._chips = mover._cash // (newstake // MIN_STAKE)
        mover._cash = mover._cash % (newstake // MIN_STAKE)
        #print("After:")
        #print(str(mover._chips))
        #print(str(mover._cash))

    def makeReport(self):
        """Report on the players that have left the casino"""

        print("Cash of highrollers:")
        for winner in self._highRollers:
            print("\t" + str(winner._cash))

        print("\nCash of bustos:")
        for busto in self._bustos:
            print("\t" + str(busto._cash))

        print("")

class Recruiter(object):
    """A recruiter that finds new players for the casino"""

    def __init__(self):
        """Setting up variables for the recruiter"""

        #No necessary variables have been identified yet

    def findPlayers(self, n):
        """Finding several players in one go"""

        recruits = list()

        for i in range(n):
            newFace = Player()
            recruits.append(newFace)

        return recruits

    def findPlayer(self):
        """Find a single player"""

        return self.findPlayers(1)
