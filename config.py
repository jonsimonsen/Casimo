"""Configuration file for Casimo"""

#Global constants

##Dealing

###hands

SUITS = 4
VALUES = 13
HAND_SIZE = 5
NUTLOW = [13, 5, 3, 2, 1]

###patterns

HICARD      = 0
PAIR        = 2
TWO_PAIR    = 22
TRIPS       = 333
LOSTRAIGHT  = 5
HISTRAIGHT  = 14
STRAIGHT    = 1234
FLUSH       = 11111
FULL_HOUSE  = 33322
QUADS       = 44441
STRFL       = 54321
NO_HAND     = -1

###testing hands

STRFLH  = [12, 11, 10, 9, 8]
STRFLM  = [47, 46, 45, 44, 43]
STRFLL  = [25, 16, 15, 14, 13]
STRH    = [25, 24, 23, 22, 8]
STRM    = [47, 7, 6, 5, 4]
STRL    = [13, 12, 3, 2, 1]
FLH     = [51, 50, 49, 40, 39]
FLL     = [5, 3, 2, 1, 0]
QHI     = [51, 38, 25, 12, 3]
QLO     = [39, 26, 13, 12, 0]
FHH     = [51, 38, 25, 13, 0]
FHL     = [39, 26, 25, 13, 12]
THI     = [51, 38, 25, 1, 0]
TMI     = [44, 31, 18, 12, 0]
TLO     = [39, 26, 13, 12, 11]
TPH     = [51, 38, 37, 24, 0]
TPM     = [47, 34, 30, 17, 6]
TPL     = [40, 27, 26, 13, 12]
PHI     = [51, 38, 37, 36, 35]
PHM     = [50, 37, 25, 23, 22]
PLM     = [40, 27, 16, 15, 13]
PLO     = [39, 26, 25, 24, 23]
HIA     = [25, 11, 2, 1, 0]
TESTIN  = [STRFLH, STRFLM, STRFLL, STRH, STRM, STRL,
           FLH, FLL, QHI, QLO, FHH, FHL, THI, TMI, TLO,
           TPH, TPM, TPL, PHI, PHM, PLM, PLO, HIA, NUTLOW]

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

###hand rankings

TRIP_K      = 1
TRIP_7      = 2
A_UP        = 3
K_UP        = 4
Q_UP        = 5
T_UP        = 6
E_UP        = 7
A_START     = 8
ACES        = 10
A_END       = 11
P_RANGE     = 3
AK_START    = 48
AK_END      = 54
AQ_START    = 55
AQ_END      = 60
AJ_START    = 61
AJ_END      = 64
TRASH       = 99

##Managers

###general

GROWRATE    = 0
