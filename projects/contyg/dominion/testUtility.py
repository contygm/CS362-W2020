# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 2019

@author: contyg
"""

import Dominion
import random
from collections import defaultdict

# description: Get player names
# input: n/a
# output: player_names
def getPlayerNames():
    player_names = ["Annie","*Ben","*Carla"]
    return player_names

# description: set the number of victory cards
# input: player_names
# output: nV (number of victory cards)
def getNumVictoryCards(player_names):
    if len(player_names) > 2:
        nV = 12
    else:
        nV = 8
    return nV

# description: set number of curses
# input: player_names
# output: nC (number of curses)
def getNumCurses(player_names):
    nC = -10 + 10 * len(player_names)
    return nC

# description: Define box items
# input: nV (number of victory cards)
# output: box
def defineBox(nV):
    # initialize box
    box = {}

    # set box options
    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*nV
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10
    return box

# description: initialize supply order
# input: n/a
# output: supply_order
def getSupplyOrder():
    supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                    3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                    4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                    5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                    6:['Gold','Adventurer'],8:['Province']}
    return supply_order

# description: Pick 10 cards from box to be in the supply.
# input: box
# output: supply
def pickBoxCards(box):
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]
    supply = defaultdict(list,[(k,box[k]) for k in random10])
    return supply

# description: Add standard supply cards to an existing supply deck. 
# input: supply, player_names, nV (number of victory cards), nC (number of curses)
# output: n/a
def addStandardSupplyCards(supply, player_names, nV, nC):
    supply["Copper"]=[Dominion.Copper()]*(60-len(player_names)*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*nV
    supply["Duchy"]=[Dominion.Duchy()]*nV
    supply["Province"]=[Dominion.Province()]*nV
    supply["Curse"]=[Dominion.Curse()]*nC

# description: Construct the Player objects
# input: player_names
# output: players
def makePlayers(player_names):
    players = []
    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))
    return players

# description: Play dominion 
# input: supply, supply_order, players)
# output: game play updates and directions
def playGame(supply, supply_order, players):
    turn  = 0
    #initialize the trash
    trash = []

    while not Dominion.gameover(supply):
        turn += 1    
        print("\r")    
        for value in supply_order:
            print (value)
            for stack in supply_order[value]:
                if stack in supply:
                    print (stack, len(supply[stack]))
        print("\r")
        for player in players:
            print (player.name,player.calcpoints())
        print ("\rStart of turn " + str(turn))    
        for player in players:
            if not Dominion.gameover(supply):
                print("\r")
                player.turn(players,supply,trash)
            
# description: calculate and display final score
# input: players
# output: prints results
def getFinalScore(players):
    dcs=Dominion.cardsummaries(players)
    vp=dcs.loc['VICTORY POINTS']
    vpmax=vp.max()
    winners=[]
    for i in vp.index:
        if vp.loc[i]==vpmax:
            winners.append(i)
    if len(winners)>1:
        winstring= ' and '.join(winners) + ' win!'
    else:
        winstring = ' '.join([winners[0],'wins!'])

    print("\nGAME OVER!!!\n"+winstring+"\n")
    print(dcs)