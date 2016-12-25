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
PD_DELTA    = 50 #For use in formula in actPre

###hand rankings

J_FULL      = 1
D_FULL      = 2
AQ_FLUSH    = 3
KT_FLUSH    = 4
JG_FLUSH    = 5
K_STRAIGHT  = 6
J_STRAIGHT  = 7
T_STRAIGHT  = 8
H_STRAIGHT  = 9
F_STRAIGHT  = 10
TRIP_A      = 11
TRIP_K      = 14
TRIP_Q      = 16
TRIP_J      = 18
TRIP_T      = 21
TRIP_I      = 23
TRIP_H      = 26
TRIP_G      = 28
TRIP_F      = 30
TRIP_E      = 33
TRIP_D      = 35
TRIP_C      = 37
TRIP_B      = 40
A_UP        = 42
K_UP        = 53
Q_UP        = 62
J_UP        = 71
T_UP        = 79
I_UP        = 86
H_UP        = 92
G_UP        = 97
F_UP        = 102
E_UP        = 105
D_UP        = 108
C_UP        = 110
P_A         = 111
P_DELTA     = 47
SFDRAW      = 320
SEQDRAW     = 370
BRDRAW      = 720
AK_HI       = 721
AQ_HI       = 814
AJ_HI       = 882
KQ_HI       = 929
AT_HI       = 997
TRASH       = 999

TRIP_X = (TRIP_B, TRIP_C, TRIP_D, TRIP_E, TRIP_F, TRIP_G, TRIP_H, TRIP_I,
          TRIP_T, TRIP_J, TRIP_Q, TRIP_K, TRIP_A)
X_UP = (C_UP, D_UP, E_UP, F_UP, G_UP, H_UP, I_UP, T_UP, J_UP, Q_UP, K_UP, A_UP)

##Managers

###general

GROWRATE    = 1
