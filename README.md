# Casimo
Casino simulator (intending to make a simulator for 5-card draw poker initially).

# Implementation
Planning to program it in Python

# Running
Run from terminal by navigating to the folder containing the py files and typing: <br />
  python casimo.py <br /> <br />
From version 0.2, the output tends to be too large for a terminal. Try writing to a file by using the syntax <br />
  python casimo.py > filename.txt <br />
Make sure that the path you choose for the output does not cause overwriting of important files. <br />
Sample output can be found in the file output.txt <br />
  
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
  -The simulator runs until there are no full tables left, and makes reports when reaching that point. <br />

v0.2: <br />
  -Added the possibility for new managers to be generated to handle higher stakes when appropriate. <br />
  -Added functionality for moving up and down between stakes based on the number of big bets in a player's chipstack. <br />
  -Added functionality to convert between cash and chips in such a fashion that 1 chip equals one small blind at every stake.  <br />
  -The cashier keeps a list of players having too much cash to play at the highest stakes (labeled high-rollers). <br />
  -Fixed a logical error that caused players to lose more chips than what they contributed to the pot at higher stakes. <br /> <br />

Minor issues: <br />
  -Fixed logical errors in conversion between chips and cash that was present in a temporary version in a side branch. <br />
  