#Global constants for a loose player

##Before draw

#LOS_B_R     = 43    #Raise range
#LOS_B_RR    = 16    #Reraise range
#LOS_B_CAP   = 10    #Capping range
#
# LOS_B_CR    = 37    #Calling a single raise
# LOS_B_CDR   = 19    #Calling a double raise
# LOS_B_CCAP  = 10    #Calling a triple raise
#
# LOOSE = (LOS_B_R, LOS_B_RR, LOS_B_CAP,
#          LOS_B_CR, LOS_B_CDR, LOS_B_CCAP)

##After draw

# LOS_A_B     = 19    #Betting range
# LOS_A_R     = 10    #Raising range
# LOS_A_RR    = 5     #Reraising range
# LOS_A_CAP   = 3     #Capping range
#
# LOS_A_CB    = 31    #Calling a single bet
# LOS_A_CR    = 19   #Calling a double raise
# LOS_A_CRR   = 10    #Calling a triple raise
# LOS_A_CCAP  = 6     #Calling a capped pot

LOS_BASE = 30       #Minimum raising hand from first position
LOS_FBOOST = 20     #Percentwise boost to minimum requirements per fold
LOS_CLIMIT = 5      #Penalty to base for calling or reraising a raiser
#(fold the worst 5 % of hands that are inside the raiser's assumed range)
