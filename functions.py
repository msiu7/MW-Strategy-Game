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
def fixTextures(grid):
    for row in range(29):
        for col in range(49):
            if isinstance(grid[row][col], landTile):
                if  (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col - 1], oceanTile) and isinstance(grid[row][col + 1], landTile)):                
                    img = pygame.image.load('CoastL.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastR.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastT.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastB.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastTR.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastBL.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastBR.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastTL.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3B.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3T.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('Coast3L.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('Coast3R.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], oceanTile) and isinstance(grid[row + 1][col], oceanTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)):
                    img = pygame.image.load('CoastPH.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], oceanTile) and isinstance(grid[row][col - 1], oceanTile)):
                    img = pygame.image.load('CoastPV.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], oceanTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDBL.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], oceanTile)):
                    img = pygame.image.load('CoastDBR.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()          
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], oceanTile) and isinstance(grid[row - 1][col + 1], landTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDTL.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()
                if (isinstance(grid[row - 1][col], landTile) and isinstance(grid[row + 1][col], landTile) and isinstance(grid[row][col + 1], landTile) and isinstance(grid[row][col - 1], landTile)
                and isinstance(grid[row - 1][col - 1], landTile) and isinstance(grid[row - 1][col + 1], oceanTile) and isinstance(grid[row + 1][col - 1], landTile) and isinstance(grid[row + 1][col + 1], landTile)):
                    img = pygame.image.load('CoastDTR.png')
                    grid[row][col].setTexture(img)
                    grid[row][col].setCoastal()

#Drawing UI Buttons
def drawUI(screen1, backgroundUI, endturn):
    pygame.draw.rect(screen1, (211, 182, 131), backgroundUI)
    pygame.draw.rect(screen1, (0, 0, 0), endturn)
    









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