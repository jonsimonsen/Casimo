#Global constants for a tight player

##Before draw

# TIG_B_R     = 19    #Raise range
# TIG_B_RR    = 5     #Reraise range
# TIG_B_CAP   = 2     #Capping range
#
# TIG_B_CR    = 10    #Calling a single raise
# TIG_B_CDR   = 3     #Calling a double raise
# TIG_B_CCAP  = 1     #Calling a triple raise
#
# TIGHT = (TIG_B_R, TIG_B_RR, TIG_B_CAP,
#          TIG_B_CR, TIG_B_CDR, TIG_B_CCAP)

##After draw

# TIG_A_B     = 3     #Betting range
# TIG_A_R     = 1     #Raising range
# TIG_A_RR    = 1     #Reraising range
# TIG_A_CAP   = 1     #Capping range
#
# TIG_A_CB    = 10    #Calling a single bet
# TIG_A_CR    = 3     #Calling a double raise
# TIG_A_CRR   = 1     #Calling a triple raise
# TIG_A_CCAP  = 1     #Calling a capped pot

TIG_BASE = 12       #Minimum raising hand from first position
LOS_FBOOST = 33     #Percentwise boost to minimum requirements per fold
LOS_CLIMIT = 12.5      #Penalty to base for calling or reraising a raiser
#(fold the worst 12.5 % of hands that are inside the raiser's assumed range)
