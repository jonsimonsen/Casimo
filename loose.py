#Global constants for a loose player

##After draw

LOS_A_B     = 19    #Betting range
LOS_A_R     = 10    #Raising range
LOS_A_RR    = 5     #Reraising range
LOS_A_CAP   = 3     #Capping range

LOS_A_CB    = 31    #Calling a single bet
LOS_A_CR    = 19   #Calling a double raise
LOS_A_CRR   = 10    #Calling a triple raise
LOS_A_CCAP  = 6     #Calling a capped pot

##Predraw

LOS_BRAN    = 520
LOS_BCFAC   = 0.12
LOS_BRFAC   = 2
LOS_BFAC    = 2.25
LOS_PRE = (LOS_BRAN, LOS_BCFAC, LOS_BRFAC, LOS_BFAC)
