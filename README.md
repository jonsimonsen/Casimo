# Casimo
Casino simulator (intending to make a simulator for 5-card draw poker initially).

# Implementation
The simulator is being programmed in Python

# Running
Run from terminal by navigating to the folder containing the py files and typing: <br />
  python casimo.py <br /> <br />
From version 0.2, the output tends to be too large for a terminal. Try writing to a file by using the syntax <br />
  python casimo.py > filename.txt <br />
Make sure that the path you choose for the output does not cause overwriting of important files. <br />
Sample output can be found in the file output.txt <br />
Version 0.3 contains code for a dealer, and can be run by typing: <br />
  python one_hand.py <br />
  
# Testing
v0.4: The largest test was run with these parameters: 50k hands/3 different stakes/32 tables per limit/GROWRATE of 1 <br />
It seems like the tight players are superior (all 5 highrollers and all players at the highest limit were tight). <br />
The loose players are getting pummeled. Only 4 loose players remained at the end. <br />
It's somewhat surprising that the regular players are not performing better. A tweak of the ranges should be considered. <br />

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
  
v0.25: <br />
  -Added a recruiter class. So far, it only contains a few methods. It should eventually be able to produce different kinds of players. <br />
  -Made some cleanup and tested at a bigger scale (3 stakes, higher number of tables, more hands played). <br /> <br />
  
Minor issues: <br />
  -Fixed erroneous global constant that caused busted players to sometimes have a negative amount of cash (from side branch). <br />
  
v0.29: <br />
  -Preparation for v0.3. <br />
  -Files dealer.py and one_hand.py. At the moment, they're separate from the rest of the files. <br />
  -Contains classes for a dealer and cards. The dealer can deal hands and print info about the cards dealt. <br />
  -Started to implement functionality for the dealer to rearrange cards in a hand and print what hand it is (straight/pair etc.) <br />

Minor issues: <br />
  -Improved the algorithm that determines the winner from v0.1 by using a global constant. <br />

v0.3: <br />
  -Finished implementing the functionality for sorting and categorising hands. <br />
  -All global constants for dealers/cards are now found in config.py (Planning to move stuff here from the other classes too). <br />
  -Functionality for testing/dealing specific hands are implemented. Not intended for use by unsophisticated users. <br />
  
Minor issues: <br />
  -Should improve message passing between some of the functions. <br />
  -Does not identify drawing hands yet. Some hands could belong in several categories (pair with draw, straight draw and flush draw etc.). <br />
  
v0.31: <br />
  -Added the ability to return sorted hands from readHand to its caller, and from dealHand to its caller (issue 1 in v0.3). <br />
  -Decided that the dealer should not be concerned with drawing (issue 2). Should probably handle this in the Player class eventually. <br />
  -Final version before trying to combine dealers with tables/managers/players. <br />
  
v0.32: <br />
  -Imports the dealer class into entities.py <br />
  -Moved global constants to config.py <br />
  -Minor refactoring and some new comments <br />

v0.35: <br />
  -Players can now play actual hands, instead of just winning randomly. The play does not yet contain a draw phase. <br />
  -Have implemented three different strats for players (loose, regular and tight). The recruiter assigns a random strat to any new player. <br />
  -The dealer has gotten a showdown function, that takes the remaining players and gives the pot to the one with the best hand. <br />
  -The pot is split if there's a tie. Leftover chips are distributed randomly between the winners (the same person can win more than one of these). <br />

Issues/shortcomings: <br />
  -There were several bugs in the first attempts. An example was related to popping from a list while in the process of iterating over it. <br />
  -A lack of a well planned design before starting on this version has led to some messy code. Some refactoring should be looked into soon. <br />
  -Doing a larger scale test, and comparing the successfulness of each strat should be added soon. <br />

v.0.4: <br />
  -The code has been partly refactored. An example is making actual getter- and setter-functions. More can be done here. <br />
  -It was looked into using heritage for some of the classes. None of the classes has enough similarities yet to make this a high priority. <br />
  -Some larger tests have been run (see the paragraph about testing). <br />
  
v0.5: <br />
  -Further refactoring, including more getters/setters and removal of some duplication. <br />
  -A decent amount of testing has been done, and the most apparent shortcommings have been fixed. Therefore, this is merged into the master branch. <br />
  
Issues/potential improvements: <br />
  -The simulator does not handle drawing cards, so currently only has one betting round. <br />
  -The player types that are available could be tweaked somewhat. An example is that the regulars seems to play slightly to loose to be able to reach high limits. <br />
  -Some values that are now manipulated directly in functions, should probably rely on setter methods instead. <br />
  -Large scale tests suggest that the code needs to be more efficient to be able to simulate a large number of hands in an acceptable amount of time. <br />
  
Summary: <br />
  -Supports multiple tables at different stakes. New players start with a reasonable stack at the lowest stakes. <br />
  -A recruiter class generates the new players by randomly picking a strategy for them (loose/regular or tight). <br />
  -A manager handles tables, using a waitlist and the recruiter to make sure that tables are running smoothly (most of the time). <br />
  -Players move up and down depending on their chip stack relative to global constants. <br />
  -The cashier takes care of players moving between stakes and leaving. Players that have left are kept in a list that can be used for statistical analysis. <br />
  -A dealer generates new hands and sorts them for the players. The dealer also distributes the pot between players at showdown. <br />
  
