#Global constants for a tight player

##After draw

TIG_A_B     = 3     #Betting range
TIG_A_R     = 1     #Raising range
TIG_A_RR    = 1     #Reraising range
TIG_A_CAP   = 1     #Capping range

TIG_A_CB    = 10    #Calling a single bet
TIG_A_CR    = 3     #Calling a double raise
TIG_A_CRR   = 1     #Calling a triple raise
TIG_A_CCAP  = 1     #Calling a capped pot

##Predraw

TIG_BRAN    = 280
TIG_BCFAC   = 0.24
TIG_BRFAC   = 4
TIG_BFAC    = 2.5
TIG_PRE = (TIG_BRAN, TIG_BCFAC, TIG_BRFAC, TIG_BFAC)
