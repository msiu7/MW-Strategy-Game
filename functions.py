import random
from landTile import landTile
import pygame

def actualBattle(player1, player2, tile1SoldierNum, tile2SoldierNum, id1, id2, grid):
    if isinstance(grid[id1 // 50][id1 % 50], landTile):
        popOffsetConst = 1;
    else:
        popOffsetConst = 0;
    '''if isinstance(grid[id2 // 50][id2 % 50], landTile):
        popOffsetConst2 = 1;
    else:
        popOffsetConst2 = 0; '''
    player1Roll = 0
    player2Roll = 0
    attackingSoldierDeathCount = 0
    defendingSoldierDeathCount = 0
    while (len(grid[id1 // 50][id1 % 50].population)) > popOffsetConst and tile1SoldierNum != 0 and tile2SoldierNum != 0:
        player1Roll = random.randint(1,6)
        player2Roll = random.randint(1,6)
        print(f"Attacker: {player1Roll}")
        print(f"Defender: {player2Roll}")
        if player1Roll > player2Roll:
            tile2SoldierNum -= 1
            defendingSoldierDeathCount += 1
            
            
             
            print("Defender lost a soldier")
            for a in range(len(grid[id2 // 50][id2 % 50].population)):
                print(f"value of statement in for loop")
                if grid[id2 // 50][id2 % 50].population[a].type == "soldier":
                    grid[id2 // 50][id2 % 50].population.pop(a)
                    print(f"Defender kill confirmed {tile2SoldierNum}")
                    break


        else:
            tile1SoldierNum -= 1
            attackingSoldierDeathCount += 1
            print("Attacker lost a soldier")
            for a in range(len(grid[id1 // 50][id1 % 50].population)):
                if grid[id1 // 50][id1 % 50].population[a].type == "soldier":
                    grid[id1 // 50][id1 % 50].population.pop(a)
                    print(f"Attacker kill confirmed {tile1SoldierNum}")
                    break

    if tile2SoldierNum == 0:
        player2.subtractTerritoryFromPlayerInWar(id2)
        player1.addTerritoryToPlayer(id2)        

    pygame.display.flip()

def findPlayerFromTile(id, players):
    for a in range(len(players)):
        for b in range(len(players[a].territories)):
            if players[a].territories[b] == id: 
                return a
    return 100

def checkPureAdjacency(id1, id2):
    if (id1 == id2 - 1):
        return True
    elif (id1 == id2 + 1):
        return True
    elif (id1 == id2 - 50):
        return True
    elif (id1 == id2 + 50):
        return True
    return False 

#Drawing UI Buttons
def drawUI(screen1, backgroundUI, endturn):
    pygame.draw.rect(screen1, (211, 182, 131), backgroundUI)
    pygame.draw.rect(screen1, (0, 0, 0), endturn)

#Work In Progess, Checks If Tile Controlled By Another Player (LITERALLY NOT USED ANYWHERE ?????)
def checkIfUsedID(id, ids):
    for a in range(0, ids.size()):
        if id == ids[a]:
            return True
    return False