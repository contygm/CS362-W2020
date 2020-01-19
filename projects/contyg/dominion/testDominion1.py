# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2019

@author: contyg
"""

import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = testUtility.getPlayerNames()

#number of curses and victory cards
nV = testUtility.getNumVictoryCards(player_names)
nC = testUtility.getNumCurses(player_names)

#Define box
box = testUtility.defineBox(nV)

# initialize supply_order
supply_order = testUtility.getSupplyOrder()

# Pick 10 cards from box to be in the supply.
supply = testUtility.pickBoxCards(box)

# The supply always has these cards.
testUtility.addStandardSupplyCards(supply, player_names, nV, nC)

# Construct the Player objects
players = testUtility.makePlayers(player_names)

#Play the game
testUtility.playGame(supply, supply_order, players)
            
#Final score
testUtility.getFinalScore(players)
