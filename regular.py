#Global constants for a regular player

##Before draw

# REG_B_R     = 31        #Raise range
# REG_B_RR    = 10        #Reraise range
# REG_B_CAP   = 5         #Capping range
#
# REG_B_CR    = 25        #Calling a single raise
# REG_B_CDR   = 6         #Calling a double raise
# REG_B_CCAP  = 3         #Calling a triple raise
#
# REGULAR = (REG_B_R, REG_B_RR, REG_B_CAP,
#            REG_B_CR, REG_B_CDR, REG_B_CCAP)

##After draw

# REG_A_B     = 10        #Betting range
# REG_A_R     = 5         #Raising range
# REG_A_RR    = 3         #Reraising range
# REG_A_CAP   = 2         #Capping range
#
# REG_A_CB    = 19        #Calling a single bet
# REG_A_CR    = 5         #Calling a double raise
# REG_A_CRR   = 3         #Calling a triple raise
# REG_A_CCAP  = 2         #Calling a capped pot

#BD

# REG_UTG     = 496       #Minimum hand for getting involved
# REG_HIJ     = 536
# REG_BTN     = 616
# REG_SB      = 830

REG_BASE = 20       #Minimum raising hand from first position
REG_FBOOST = 25     #Percentwise boost to minimum requirements per fold
REG_CLIMIT = 10      #Penalty to base for calling or reraising a raiser
#(fold the worst 10 % of hands that are inside the raiser's assumed range)

STRAT = [REG_BASE, REG_FBOOST, REG_CLIMIT]
