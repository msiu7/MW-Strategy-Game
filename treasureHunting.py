import random
from classes import *

#code for ocean spelunking mechanic

def triggerRandomEvent(player):
    a = random.randrange(0, 5)
    b = random.randrange(1, 21)
    if a == 0:
        player.lastTurnGoldFromTreasure += b
    elif a == 1:
        player.lastTurnBrickFromTreasure += b 
    elif a == 2:
        player.lastTurnFoodFromTreasure += b 
    elif a == 3:
        player.lastTurnStoneFromTreasure += b
    else:
        player.lastTurnWoodFromTreasure += b

#goes through all ocean tiles that belong to a player and randomly decides whether treasure is found or not
def checkSpelunk(player):
    player.lastTurnGoldFromTreasure = 0
    player.lastTurnBrickFromTreasure = 0 
    player.lastTurnFoodFromTreasure = 0 
    player.lastTurnStoneFromTreasure = 0
    player.lastTurnWoodFromTreasure = 0
    for a in range(0, len(player.territories)):
        randomize = random.randrange(0, 100)
        print(randomize)
        if (isinstance(player.territories[a], oceanTile) and randomize < player.territories[a].spelunkingChance and player.territories[a].spelunkingCooldown <= 0):
            triggerRandomEvent(player)
            player.territories[a].spelunkingCooldown = 10

def reduceTreasureCooldown(player):
    for a in range(0, len(player.territories)):
        if player.territories[a].spelunkingCooldown != 0:
            player.territories[a].spelunkingCooldown -= 1

