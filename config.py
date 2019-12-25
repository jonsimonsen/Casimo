"""Configuration file for Casimo"""

#Global constants

##General
HANDS_PER_ROUND = 20    #Number of hands played in each round (per table)
ROUNDS = 10             #Number of rounds to run the simulator
HEADING = 'Welcome to Casimo, the casino simulator.\n\n'
TAILING = 'It will simulate ' + str(ROUNDS) + ' rounds of poker hands with ' + str(HANDS_PER_ROUND) + ' hands per round.\n'
GREETING = HEADING + TAILING

##Dealing

###hands/cards

CLUBS       = 0
DIAMONDS    = 1
HEARTS      = 2
SPADES      = 3
SUITS       = (CLUBS, DIAMONDS, HEARTS, SPADES)
MIN_RANK    = 2     #deuces
MAX_RANK    = 14    #aces
HAND_SIZE   = 5
NUTLOW      = [13, 5, 3, 2, 1]

###patterns

HICARD      = 0
BWDRAW      = 1     #Broadway draw
STRDRAW     = 5     #Assumed to be open ender
FLDRAW      = 10
STRFLDRAW   = 15
PBWDRAW     = 21
PSTRDRAW    = 52
PFLDRAW     = 102
PSTRFLDRAW  = 152
PAIR        = 211
TWO_PAIR    = 221
TRIPS       = 333
STRAIGHT    = 12345
FLUSH       = 22222
FULL_HOUSE  = 33322
QUADS       = 44441
STRFL       = 54321
NO_HAND     = -1

###patterns that needs sorting
UNSTR   = 6
UNFL    = 11
UNSTRFL = 16
UNPFL   = 103
UNPSF   = 153

##Tables

###general

MIN_STAKE = 4       #Number of chips for a big bet at the smallest stakes
MAX_STAKE = 16      #Number of chips for a big bet at the highest stakes
BUY_IN = 120        #Number of big bets required to sit down at a table
MAX_TABLES = 32     #Maximum amount of tables at a stake
SEATS = 5           #Number of seats at a table
MAX_BETS = 6        #Maximum number of big bets per player per hand

###for moving between stakes
MAX_STACK = BUY_IN * 2          #When posting the BB, this is the max amount of big bets allowed (must move up otherwise)
MIN_STACK = BUY_IN // 2         #When posting the BB, this is the least amount of big bets allowed (must move down otherwise)
MIN_UNITS = MAX_BETS * SEATS    #When posting the BB at the lowest stakes, this is the least amount of big bets allowed (must leave otherwise)

##Players

###general

SEATED      = 0
MOVE_UP     = 1
MOVE_DOWN   = 2
BUSTO       = 3

###hand rankings

#K_FULL      = 1
#T_FULL      = 2
#F_FULL      = 3
#A_FLUSH     = 4
#J_FLUSH     = 6
#A_STRAIGHT  = 8
#T_STRAIGHT  = 12
#E_STRAIGHT  = 16
#TRIP_A      = 24
#TRIP_Q      = 32
#TRIP_I      = 48
#TRIP_B      = 64
#A_UP        = 96
#Q_UP        = 128
#C_UP        = 192
#P_A         = 256
#P_DELTA     = 40
#SFDRAW      = 420
#SEQDRAW     = 480
#BRDRAW      = 700
#AK_HI       = 780
#AQ_HI       = 830
#AJ_HI       = 870
#AT_HI       = 940   #Includes KQ-hi
#TRASH       = 999

###hand ratings (planning to replace the rankings with these)
TRIP_K = 1
TRIP_7 = 2
A_UP = 3
K_UP = 4
J_UP = 5
I_UP = 6
G_UP = 7
ACES = range(8, 11)
KINGS = range(11, 15)
QUEENS = range(15, 18)
JACKS = range(18, 21)
TENS = range(21, 24)
NINES = range(24, 28)
EIGHTS = range(28, 31)
SEVENS = range(31, 34)
SIXES = range(34, 37)
FIVES = range(37, 41)
FOURS = range(41, 44)
THREES = range(44, 47)
DEUCES = range(47, 50)
AK_HI = range(50, 56)
AQ_HI = range(56, 62)
AJ_HI = range(62, 65)
AT_HI = range(65, 67)
A_HI = range(67, 70)
KQ_HI = range(70, 74)
KJ_HI = range(74, 78)
KT_HI = range(78, 80)
K_HI = range(80, 83)
QJ_HI = range(83, 86)
QT_HI = range(86, 88)
Q_HI = range(88, 91)
JT_HI = range(91, 93)
J_HI = range(93, 95)
T_HI = range(95, 98)
I_HI = range(98, 100)

##Managers

###general

GROWRATE    = 1
