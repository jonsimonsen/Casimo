# Casimo
Casino simulator (intending to make a simulator for 5-card draw poker initially).

# Implementation
Planning to program it in Python

# Running
Run from terminal by navigating to the folder containing the py files and typing: 
  python casimo.py
  
# History
v0.1: <br />
  -Number of rounds simulated is determined by a global constant. <br />
  -Made an algorithm for one five-man table: <br />
    -Every player bets the maximum amount each hand. <br />
    -No cards are drawn (or all players draw in the same way) <br />
    -Ties are not possible. (If several players have the same hand, rank by suit or by coinflipping) <br />
  -After each hand, the chip count for the players are output (tested in terminal/cmd) <br />

v0.15: <br />
  -Added a cashier class to give players cash when they leave and keep a list of these players. <br />
  -The stake manager now removes busted from a table and directs them to the cashier. <br />
  -Tables that are not full are kept in a separate list from full tables. <br />
  -The simulator runs until there are no full tables left, and makes reports when reaching that point.
