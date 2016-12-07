"""Test hand templates for Casimo"""

#sorted

##STRFL
RSTRFLC     = [12, 11, 10,  9,  8]
RSTRFLD     = [25, 24, 23, 22, 21]
RSTRFLH     = [38, 37, 36, 35, 34]
RSTRFLS     = [51, 50, 49, 48, 47]
KSTRFL      = [50, 49, 48, 47, 46]
FSTRFL      = [43, 42, 41, 40, 39]
ESTRFLS     = [42, 41, 40, 39, 47] #Ace 4 spots sooner bc of popping
ESTRFLC     = [ 3,  2,  1,  0,  8]
TSTRFL = [RSTRFLC, RSTRFLD, RSTRFLH, RSTRFLS, KSTRFL, FSTRFL, ESTRFLS, ESTRFLC]

##Quads/FH
QUADA       = [51, 38, 25, 12, 11]
QUADK       = [50, 37, 24, 11, 11]
QUADB       = [39, 26, 13,  0, 11]
FULLA       = [51, 38, 25, 24, 11]
FULLK       = [50, 37, 24, 24, 12]
FULLB       = [39, 26, 13, 24, 12]
TQFH = [QUADA, QUADK, QUADB, FULLA, FULLK, FULLB]

##Flushes
RFLC        = [12, 11, 10,  9,  7]
RFLD        = [25, 24, 23, 22, 20]
RFLH        = [38, 37, 36, 35, 33]
RFLS        = [51, 50, 49, 48, 46]
LFLC        = [ 5,  3,  2,  1,  0]
LFLS        = [44, 42, 41, 40, 39]
RFLX        = [51, 50, 49, 47, 46]
RFLY        = [51, 50, 48, 47, 46]
RFLZ        = [51, 49, 48, 47, 45]
RFLZO       = [51, 49, 48, 47, 46]
WFL         = [51, 43, 41, 40, 39]
WFLX        = [51, 43, 42, 40, 39]
WFLY        = [51, 43, 42, 41, 39]
WFLZ        = [51, 44, 42, 41, 40]
WFLZO       = [51, 43, 42, 41, 40]
TFL = [RFLC, RFLD, RFLH, RFLS, LFLC, LFLS, RFLX, RFLY, RFLZ, RFLZO,
       WFL, WFLX, WFLY, WFLZ, WFLZO]

##Straights
RSTR        = [25, 11, 10,  9,  8]
KSTR        = [24, 10,  9,  8,  7]
FSTR        = [17,  3,  2,  1,  0]
ESTR        = [ 3,  2,  1,  0, 21] #Ace 4 spots sooner bc of popping
TSTR = [RSTR, KSTR, FSTR, ESTR]

##Trips
TRIPA       = [51, 38, 25, 24, 23]
TRIPK       = [50, 37, 24, 12, 10]
TRIPB       = [39, 26, 13, 12, 11]
TTRIP = [TRIPA, TRIPK, TRIPB]

##Two Pairs
AUPK        = [51, 38, 24, 11,  0]
AUPB        = [51, 38, 26, 13, 11]
KUPB        = [50, 37, 26, 13, 10]
CUPB        = [40, 27, 26, 13, 12]
TPAIRS = [AUPK, AUPB, KUPB, CUPB]

##Pair
ACESON      = [51, 38, 37, 36, 35]
KINGSON     = [50, 37, 25, 23, 22]
DUCKSON     = [39, 26, 25, 24, 23]
DUCKSOL     = [39, 26, 16, 15, 14]
TREYSOL     = [40, 27, 16, 15, 13]
TPAIR = [ACESON, KINGSON, DUCKSON, DUCKSOL, TREYSOL]

##Hicard
HIAON       = [51, 50, 49, 48, 33]
HIAOL       = [51, 43, 41, 40, 26]
HIGON       = [44, 42, 41, 40, 26]
THI = [HIAON, HIAOL, HIGON]

TSORT = [TSTRFL, TQFH, TFL, TSTR, TTRIP, TPAIRS, TPAIR, THI]

#unsorted

##STRFL
URSTRFL     = [11,  9,  8,  9,  8]
UKSTRFL     = [50, 46, 46, 46, 46]
UESTRFL     = [39, 39, 40, 39, 39] #Ace 4 spots sooner bc of popping
UTSTRFL = [URSTRFL, UKSTRFL, UESTRFL]

##Quads/FH
UQUADA      = [51, 38, 25, 36, 12] #AK
UQUADK      = [51, 37, 49, 11, 23] #KA
UQUADB      = [26, 13, 24,  0, 35] #2A
UFULLA      = [24, 24, 36, 48, 11] #AK
UFULLK      = [50, 37, 24, 12, 35] #KA
UFULLB      = [13, 50, 25, 24, 36] #2A
UTQFH = [UQUADA, UQUADK, UQUADB, UFULLA, UFULLK, UFULLB]

##Flushes
URFL        = [46, 47, 48, 47, 47]
ULFL        = [ 5,  3,  2,  0,  0]
UWFL        = [43, 40, 49, 40, 39]
UTFL = [URFL, ULFL, UWFL]

##Straights
URSTR       = [11, 10,  9,  8, 21]
UKSTR       = [23, 21, 11, 20, 19]
UESTR       = [ 0,  0,  0,  0, 47] #Ace 4 spots sooner bc of popping
UTSTR = [URSTR, UKSTR, UESTR]

##Trips
#TRIPA       = [51, 38, 25, 24, 23]
#TRIPK       = [50, 37, 24, 12, 10]
#TRIPB       = [39, 26, 13, 12, 11]
#TTRIP = [TRIPA, TRIPK, TRIPB]

##Two Pairs
#AUPK        = [51, 38, 24, 11,  0]
#AUPB        = [51, 38, 26, 13, 11]
#KUPB        = [50, 37, 26, 13, 10]
#CUPB        = [40, 27, 26, 13, 12]
#TPAIRS = [AUPK, AUPB, KUPB, CUPB]

##Pair
#ACESON      = [51, 38, 37, 36, 35]
#KINGSON     = [50, 37, 25, 23, 22]
#DUCKSON     = [39, 26, 25, 24, 23]
#DUCKSOL     = [39, 26, 16, 15, 14]
#TREYSOL     = [40, 27, 16, 15, 13]
#TPAIR = [ACESON, KINGSON, DUCKSON, DUCKSOL, TREYSOL]

##Hicard
#HIAON       = [51, 50, 49, 48, 33]
#HIAOL       = [51, 43, 41, 40, 26]
#HIGON       = [44, 42, 41, 40, 26]
#THI = [HIAON, HIAOL, HIGON]

TUNSORT =[UTSTRFL, UTQFH, UTFL, UTSTR]
