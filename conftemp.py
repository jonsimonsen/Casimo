"""Configuration file for Casimo"""

#Global constants

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

###general

SEATED      = 0
MOVE_UP     = 1
MOVE_DOWN   = 2
BUSTO       = 3

###hand rankings

K_FULL      = 1
T_FULL      = 2
6_FULL      = 3
A_FLUSH     = 4
J_FLUSH     = 6
A_STRAIGHT  = 8
T_STRAIGHT  = 12
5_STRAIGHT  = 16
TRIP_A      = 24
TRIP_Q      = 32
TRIP_9      = 48
TRIP_2      = 64
A_UP        = 96
Q_UP        = 128
3_UP        = 192
P_A         = 256
P_DELTA     = 40
SFDRAW      = 420
SEQDRAW     = 480
BRDRAW      = 700
AK_HI       = 780
AQ_HI       = 830
AJ_HI       = 870
AT_HI       = 940   #Includes KQ-hi
TRASH       = 999

##Managers

###general

GROWRATE    = 1
