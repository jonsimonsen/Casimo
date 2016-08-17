# Casimo
Casino simulator (intending to make a simulator for 5-card draw poker initially).

# Implementation
Planning to program it in Python

# Running
Run from terminal by navigating to the folder containing the py files and typing: 
  python casimo.py
  
# History
v0.1: 
  -Number of rounds simulated is determined by a global constant.
  -Made an algorithm for one five-man table:
    -Every player bets the maximum amount each hand.
    -No cards are drawn (or all players draw in the same way)
    -Ties are not possible. (If several players have the same hand, rank by suit or by coinflipping)
  -After each hand, the chip count for the players are output (tested in terminal/cmd)
