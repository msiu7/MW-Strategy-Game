import random
from classes import *

#Random Walk Land Generation
def genLand(xx, yy, grid):
    x = xx
    y = yy
    while (x < 49 and x > 1) and (y < 29 and y > 1):
        grid[y][x] = landTile(x*25, y*25, 25, 25)
        grid[y + 1][x] = landTile(x*25, (y+1)*25, 25, 25)
        grid[y - 1][x] = landTile(x*25, (y-1)*25, 25, 25)
        grid[y][x + 1] = landTile((x+1)*25, y*25, 25, 25)
        grid[y][x - 1] = landTile((x-1)*25, y*25, 25, 25)
        choice = random.randrange(1, 5)
        if choice == 1:
            y -= 1
        elif choice == 2:
            y += 1
        elif choice == 3:
            x -= 1
        else:
            x += 1

#Removes Ocean Tiles Surrounded By Land
def removeIsolatedOcean(grid):
    for row in range(1, 29):
        for col in range(1, 49):  
            if isinstance(grid[row][col], oceanTile):
                surrounded_by_land = (
                    isinstance(grid[row - 1][col], landTile) and
                    isinstance(grid[row + 1][col], landTile) and
                    isinstance(grid[row][col - 1], landTile) and
                    isinstance(grid[row][col + 1], landTile)
                )
                if surrounded_by_land:
                    grid[row][col] = landTile(col * 25, row * 25, 25, 25)

#Returns Total Land Tiles
def checkTotalLand(grid):
    counter = 0
    for row in range(30):
        for col in range(50):
            if isinstance(grid[row][col], landTile):
                counter += 1
    return counter

#Checks if there is a "perfect" amount of land tiles
def isValidGen(grid):
    if (checkTotalLand(grid) > 575 and checkTotalLand(grid) < 700):
        return True
    return False

#Work In Progess, Checks If Tile Controlled By Another Player
def checkIfUsedID(id, ids):
    for a in range(0, ids.size()):
        if id == ids[a]:
            return True
    return False
    
#Develop Mountains
def CreateMountains(grid):
    foundLand = True
    row = random.randrange(1, 29)
    col = random.randrange(1, 49)
    while foundLand:
        if (isinstance(grid[row][col], landTile)):
            foundLand = False
        else:
            row = random.randrange(1, 29)
            col = random.randrange(1, 49) 
    hOrV = random.randrange(1, 3)
    if hOrV == 1:
        while (isinstance(grid[row][col], landTile) and row < 29 and col < 49 and surroundedByLand(grid, row ,col)):
            grid[row][col] = mountainTile(col * 25, row * 25, 25, 25)
            choice = random.randrange(1, 16)
            if choice < 7:
                row += 1
            elif choice < 14:
                row -= 1
            elif choice == 14:
                col += 1
            else:
                col -= 1
    else:
        while (isinstance(grid[row][col], landTile) and row < 29 and col < 49 and surroundedByLand(grid, row ,col)):
            grid[row][col] = mountainTile(col * 25, row * 25, 25, 25)
            choice = random.randrange(1, 16)
            if choice < 7:
                col += 1
            elif choice < 14:
                col -= 1
            elif choice == 14:
                row += 1
            else:
                row -= 1          

def randomizeTextures(grid):
    for row in range(29):
        for col in range(50):
            # #Normal Land Tile
            # if (grid[row][col])


            #Forest Tile
            if (isinstance(grid[row][col], forestTile)):
                rand = random.randrange(1, 5)
                if rand == 2:
                    img = pygame.image.load('forest1.png')
                    grid[row][col].setTexture(img)
                if rand == 3:
                    img = pygame.image.load('forest2.png')
                    grid[row][col].setTexture(img)             
                if rand == 4 or rand == 5:
                    img = pygame.image.load('forest3.png')
                    grid[row][col].setTexture(img)

def surroundedByLand(grid, row, col):
    if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile) and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
        return True
    return False

def checkTotalMountain(grid):
    count = 0
    for row in range(30):
        for col in range(50):
            if isinstance(grid[row][col], mountainTile):
                count += 1
    return count




#Gives Proper Coastal Texture To All Land Tiles
def fixCoastalTextures(grid):
    for row in range(29):
        for col in range(49):
            if isinstance(grid[row][col], landTile):
                if  (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col - 1], oceanTile) and isinstance(grid[row][col + 1], landTile)):                
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastT.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastB.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastTR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastBL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastBR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastBR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastTL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('Coast3B.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('Coast3T.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('Coast3L.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('Coast3R.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastPH.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastPV.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], oceanTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastDBL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], oceanTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastDBR.png')
                    grid[row][col].setTexture(img)         
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], oceanTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastDTL.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], oceanTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                    img = pygame.image.load('CoastDTR.png')
                    grid[row][col].setTexture(img)
            
def fixMountainTextures(grid):
    for row in range(29):
        for col in range(49):  
            if isinstance(grid[row][col], mountainTile):
                if  (not isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col - 1], mountainTile) and not isinstance(grid[row][col + 1], mountainTile)):                
                    img = pygame.image.load('MountainL.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainT.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainB.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainTR.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainBL.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainBR.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainTL.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col - 1], mountainTile) and isinstance(grid[row][col + 1], mountainTile)):
                    img = pygame.image.load('Mountain3B.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('Mountain3T.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('Mountain3L.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('Mountain3R.png')
                    grid[row][col].setTexture(img)
                if (not isinstance(grid[row - 1][col], mountainTile) and not isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1],mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainH.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and not isinstance(grid[row][col + 1], mountainTile) and not isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainV.png')
                    grid[row][col].setTexture(img)
                if (isinstance(grid[row - 1][col], mountainTile) and isinstance(grid[row + 1][col], mountainTile) and isinstance(grid[row][col + 1], mountainTile) and isinstance(grid[row][col - 1], mountainTile)):
                    img = pygame.image.load('MountainA.png')
                    grid[row][col].setTexture(img)



#Drawing UI Buttons
def drawUI(screen1, backgroundUI, endturn):
    pygame.draw.rect(screen1, (211, 182, 131), backgroundUI)
    pygame.draw.rect(screen1, (0, 0, 0), endturn)

def istileowned( cordx, cordy,players,grid, numplayers):
    tilex=cordx
    tiley=cordy
    tileid = grid[tiley][tilex].getID()
    #targettile= grid[tiley][tilex]
    for y in range (numplayers):
        for x in range (len(players[y].territories)):
            if (players[y].territories[x]==tileid):
                return True 
    return False
                

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




#Develop Forest
def CreateForest(grid):
    foundLand = True
    row = random.randrange(1, 29)
    col = random.randrange(1, 49)
    while foundLand:
        if (isinstance(grid[row][col], landTile)):
            foundLand = False
        else:
            row = random.randrange(1, 29)
            col = random.randrange(1, 49) 
    while (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col - 1], landTile) and isinstance(grid[row][col + 1], landTile)
    and row < 29 and col < 49 and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile) and isinstance(grid[row - 1][col + 1], landTile)):    
        grid[row][col] = forestTile(col*25, row*25, 25, 25)
        choice = random.randrange(1, 5)
        if choice == 1:
            row -= 1
        elif choice == 2:
            row += 1
        elif choice == 3:
            col -= 1
        else:
            col += 1


def createPlainsTiles(grid):
    for row in range(30):
        for col in range(50):
            if isinstance(grid[row][col], landTile):
                if not (isinstance(grid[row][col], coastalTile) or isinstance(grid[row][col], forestTile) or isinstance(grid[row][col], mountainTile)):
                    grid[row][col] = plainsTile(col * 25, row * 25, 25, 25)



def giveTilesProduction(grid):
    for row in range(30):
        for col in range(50):
            grid[row][col].setProduction()

def landBattle(player1, player2, tile1, tile2):
    fighting = True 
    
    SCREEN_WIDTH = 1250
    SCREEN_HEIGHT = 850
    screen0 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    Background_color = (48, 55, 191)
    screen0.fill(Background_color)
    mainSquare = pygame.Rect(300, 100, 650, 650)
    pygame.draw.rect(screen0, (0, 255, 0), mainSquare)
    while fighting == True:
        print("working")
        pygame.display.flip()
        

def actualBattle(player1, player2, tile1SoldierNum, tile2SoldierNum, id1, id2, grid):   
    player1Roll = 0
    player2Roll = 0
    attackingSoldierDeathCount = 0
    defendingSoldierDeathCount = 0
    while tile1SoldierNum != 0 and tile2SoldierNum != 0:
        player1Roll = random.randint(1,6)
        player2Roll = random.randint(1,6)
        print(f"Attacker: {player1Roll}")
        print(f"Defender: {player2Roll}")
        if player1Roll > player2Roll:
            tile2SoldierNum -= 1
            defendingSoldierDeathCount += 1
            
            
            #krv experiment
            print("Defender lost a soldier")
            for a in range((len(grid[id2 // 50][id2 % 50].population))-1):
                if grid[id2 // 50][id2 % 50].population[a].type == "soldier":
                    grid[id2 // 50][id2 % 50].population.pop(a)
                    print(f"Defender kill confirmed {tile2SoldierNum-defendingSoldierDeathCount}")
                    break


        else:
            tile1SoldierNum -= 1
            attackingSoldierDeathCount += 1
            print("Attacker lost a soldier")
            for a in range((len(grid[id1 // 50][id1 % 50].population))-1):
                if grid[id1 // 50][id1 % 50].population[a].type == "soldier":
                    grid[id1 // 50][id1 % 50].population.pop(a)
                    print(f"Attacker kill confirmed {tile1SoldierNum-attackingSoldierDeathCount}")
                    break

    if tile2SoldierNum == 0:
        player2.subtractTerritoryFromPlayer(id2)
        player1.addTerritoryToPlayer(id2)
        pygame.display.flip()
        

    pygame.display.flip()
    
    
    
    
    '''
    b = 0
    if tile1SoldierNum != 0:
        for a in range((len(grid[id1 // 50][id1 % 50].population))-1):
            print("preyes")
            if b == attackingSoldierDeathCount:
                break
            if grid[id1 // 50][id1 % 50].population[a].type == "soldier":  
                print("yes")
                grid[id1 // 50][id1 % 50].population.pop(a)
                a = 0
                b += 1
        for a in range((len(grid[id2 // 50][id2 % 50].population))-1):
            if grid[id2 // 50][id2 % 50].population[a].type == "soldier":  
                print("hi")
                grid[id2 // 50][id2 % 50].population.pop(a)
                a -= 1
        player2.subtractTerritoryFromPlayer(id2)
        player1.addTerritoryToPlayer(id2)

    else:
        for a in range((len(grid[id2 // 50][id2 % 50].population))-1):
            if b == defendingSoldierDeathCount:
                break
            if grid[id2 // 50][id2 % 50].population[a].type == "soldier":
                print("wsg")  
                grid[id2 // 50][id2 % 50].population.pop(a)
                a = 0
                b += 1
            
        for a in range((len(grid[id1 // 50][id1 % 50].population))-1):
            if grid[id1 // 50][id1 % 50].population[a].type == "soldier":
                print("hello") 
                grid[id1 // 50][id1 % 50].population.pop(a)
                a -= 1
        
    pygame.display.flip()'''

def findPlayerFromTile(id, players):
    for a in range(len(players)):
        for b in range(len(players[a].territories)):
            if players[a].territories[b] == id: 
                return a
    return 100
