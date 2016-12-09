"""Test hand templates for Casimo"""

#Sorted

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

###All
TSORT = [TSTRFL, TQFH, TFL, TSTR, TTRIP, TPAIRS, TPAIR, THI]

#Unsorted

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
UTRIPA       = [38, 38, 38, 25, 47] #A32
UTRIPK       = [24, 35, 49, 35, 47] #KAQ
UTRIPB       = [39, 11, 11, 11, 23] #2AK
UTTRIP = [UTRIPA, UTRIPK, UTRIPB]

##Two Pairs
UAUPK        = [51, 38, 11, 23,  0] #AK2
UAUPB        = [51, 13, 25, 11, 35] #A2K
UKUPB        = [13, 48, 36, 25, 46] #K2Q
UCUPB        = [51, 13, 13, 24, 24] #32A
UTPAIRS = [UAUPK, UAUPB, UKUPB, UCUPB]

##Pair
UACESON      = [37, 36, 49, 35, 35] #AKQJ
UKINGSON     = [37, 22, 23, 22, 22] #KAQJ
UDUCKSON     = [26, 25, 23, 36, 23] #2AKQ
UDUCKSOL     = [15, 15, 24, 36, 14] #2543
UTREYSOL     = [27, 13, 15, 37, 14] #3542
UTPAIR = [UACESON, UKINGSON, UDUCKSON, UDUCKSOL, UTREYSOL]

##Hicard
UHIAON       = [49, 49, 33, 48, 47]
UHIAOL       = [26, 40, 39, 48, 40]
UHIGON       = [44, 40, 26, 40, 39]
UTHI = [UHIAON, UHIAOL, UHIGON]

###All
TUNSORT =[UTSTRFL, UTQFH, UTFL, UTSTR, UTTRIP, UTPAIRS, UTPAIR, UTHI]

#Draws

##Paired

###STRFL
HPOESTRFL   = [50, 37, 36, 35, 34]
LPOESTRFL   = [42, 41, 40, 39, 26]
HPBWSTRFL   = [51, 50, 49, 48, 38]
HPLBWSTRFL  = [51, 49, 48, 47, 38]
LPBWSTRFL   = [51, 50, 49, 48, 35]
LPLBWSTRFL  = [51, 50, 49, 47, 34]
HPWSTRFL    = [51, 12,  2,  1,  0]
HPHWSTRFL   = [51, 12,  3,  2,  1]
LPWSTRFL    = [13, 12,  2,  1,  0]
LPHWSTRFL   = [13, 12,  3,  1,  0]
PTSTRFL = [HPOESTRFL, LPOESTRFL, HPBWSTRFL, HPLBWSTRFL, LPBWSTRFL, LPLBWSTRFL,
           HPWSTRFL, HPHWSTRFL, LPWSTRFL, LPHWSTRFL]

###FLUSH
HPFL        = [51, 38, 37, 36, 33]
LPFL        = [51, 50, 49, 46, 33]
PTFL = [HPFL, LPFL]

###STRAIGHT
HPOESTR     = [50, 49, 37, 35, 34]
LPOESTR     = [42, 41, 39, 27, 26]
HPBW        = [51, 50, 38, 36, 35]
HPLBW       = [51, 49, 38, 35, 34]
LPBW        = [51, 50, 48, 36, 35]
LPLBW       = [51, 50, 47, 36, 34]
HPW         = [51, 39, 12,  2,  1]
HPHW        = [51, 42, 12,  2,  1]
LPW         = [14, 13, 12,  2,  0]
LPHW        = [14, 13, 12,  3,  0]
PTSTR = [HPOESTR, LPOESTR, HPBW, HPLBW, LPBW, LPLBW, HPW, HPHW, LPW, LPHW]

TPSORT = [PTSTRFL, PTFL, PTSTR]

##Unpaired

###Fake (STRFL)
FHOESTRFL   = [50, 49, 48, 47, 38]
LFHOESTRFL  = [50, 49, 48, 47, 33]
FLOESTRFL   = [42, 41, 40, 39, 38]
HFLOESTRFL  = [42, 41, 40, 39, 30]
FBWFL       = [51, 50, 49, 48, 34]
FLBWFL      = [51, 49, 48, 47, 37]
FKGSFL      = [50, 49, 47, 46, 35]
FFGSFL      = [43, 42, 41, 39, 27]
FWFL        = [42, 41, 40, 39, 30]
FHWFL       = [43, 42, 41, 39, 27]

FSTRFL = [FHOESTRFL, LFHOESTRFL, FLOESTRFL, HFLOESTRFL,
          FBWFL, FLBWFL, FKGSFL, FFGSFL, FWFL, FHWFL]

###STRFL
HOESTRFL    = [50, 49, 48, 47, 32]
LOESTRFL    = [42, 41, 40, 39, 31]
BWFL        = [51, 50, 49, 48, 33]
LBWFL       = [51, 49, 48, 47, 32]
KGSFL       = [50, 49, 47, 46, 31]
FGSFL       = [43, 42, 41, 39, 32]
WFL         = [51, 41, 40, 39, 30]
HWFL        = [51, 42, 41, 40, 31]

DSTRFL = [HOESTRFL, LOESTRFL, BWFL, LBWFL, KGSFL, FGSFL, WFL, HWFL]

###STR and FL
HOEFL       = [50, 49, 48, 45, 34]
HOELFL      = [51, 49, 48, 46, 34]
LOEFL       = [44, 41, 40, 39, 29]
LOEHFL      = [51, 43, 41, 40, 29]
BWPFL       = [51, 50, 49, 46, 35]
LBWPFL      = [49, 48, 47, 44, 38]
WPFL        = [44, 41, 40, 39, 38]
HWPFL       = [51, 44, 42, 41, 27]

DSTRPFL = [HOEFL, HOELFL, LOEFL, LOEHFL, BWPFL, LBWPFL, WPFL, HWPFL]

###FLUSH
HFL = [51, 50, 49, 46, 32]
KFL = [50, 49, 46, 45, 38]
CFL = [45, 44, 41, 40, 26]
BFL = [44, 41, 40, 39, 32]

DFLUSH = [HFL, KFL, CFL, BFL]

###STRAIGHT
HSTR    = [50, 49, 48, 34, 31]
LSTR    = [42, 41, 40, 32, 26]
BW      = [51, 50, 49, 35, 32]
LBW     = [49, 48, 47, 38, 31]
WHEEL   = [51, 44, 28, 27, 26]
HWHEEL  = [42, 41, 40, 38, 32]

DSTR = [HSTR, LSTR, BW, LBW, WHEEL, HWHEEL]

TDSORT = [DSTRFL, DSTRPFL, DFLUSH, DSTR]
