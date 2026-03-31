import random
from landTile import landTile
from oceanTile import oceanTile
from mountainTile import mountainTile
from forestTile import forestTile
from coastalTile import coastalTile
from plainsTile import plainsTile
import pygame

#Random Walk Land Generation
class gameMap():

    def __init__(self):
        self.grid = []

    def genLand(self, xx, yy):
        x = xx
        y = yy
        while (x < 49 and x > 1) and (y < 29 and y > 1):
            self.grid[y][x] = landTile(x*25, y*25, 25, 25)
            self.grid[y + 1][x] = landTile(x*25, (y+1)*25, 25, 25)
            self.grid[y - 1][x] = landTile(x*25, (y-1)*25, 25, 25)
            self.grid[y][x + 1] = landTile((x+1)*25, y*25, 25, 25)
            self.grid[y][x - 1] = landTile((x-1)*25, y*25, 25, 25)
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
    def removeIsolatedOcean(self):
        for row in range(1, 29):
            for col in range(1, 49):  
                if isinstance(self.grid[row][col], oceanTile):
                    surrounded_by_land = (
                        isinstance(self.grid[row - 1][col], landTile) and
                        isinstance(self.grid[row + 1][col], landTile) and
                        isinstance(self.grid[row][col - 1], landTile) and
                        isinstance(self.grid[row][col + 1], landTile)
                    )
                    if surrounded_by_land:
                        self.grid[row][col] = landTile(col * 25, row * 25, 25, 25)

    #Returns Total Land Tiles
    def checkTotalLand(self):
        counter = 0
        for row in range(30):
            for col in range(50):
                if isinstance(self.grid[row][col], landTile):
                    counter += 1
        return counter

    #Checks if there is a "perfect" amount of land tiles
    def isValidGen(self):
        if (self.checkTotalLand() > 575 and self.checkTotalLand() < 700):
            return True
        return False
        
    #Develop Mountains
    def CreateMountains(self):
        foundLand = True
        row = random.randrange(1, 29)
        col = random.randrange(1, 49)
        while foundLand:
            if (isinstance(self.grid[row][col], landTile)):
                foundLand = False
            else:
                row = random.randrange(1, 29)
                col = random.randrange(1, 49) 
        hOrV = random.randrange(1, 3)
        if hOrV == 1:
            while (isinstance(self.grid[row][col], landTile) and row < 29 and col < 49 and self.surroundedByLand(row, col)):
                self.grid[row][col] = mountainTile(col * 25, row * 25, 25, 25)
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
            while (isinstance(self.grid[row][col], landTile) and row < 29 and col < 49 and self.surroundedByLand(row, col)):
                self.grid[row][col] = mountainTile(col * 25, row * 25, 25, 25)
                choice = random.randrange(1, 16)
                if choice < 7:
                    col += 1
                elif choice < 14:
                    col -= 1
                elif choice == 14:
                    row += 1
                else:
                    row -= 1          

    def randomizeTextures(self):
        for row in range(29):
            for col in range(50):
                # #Normal Land Tile
                # if (self.grid[row][col])


                #Forest Tile
                if (isinstance(self.grid[row][col], forestTile)):
                    rand = random.randrange(1, 5)
                    if rand == 2:
                        img = pygame.image.load('Graphics/forest1.png')
                        self.grid[row][col].setTexture(img)
                    if rand == 3:
                        img = pygame.image.load('Graphics/forest2.png')
                        self.grid[row][col].setTexture(img)             
                    if rand == 4 or rand == 5:
                        img = pygame.image.load('Graphics/forest3.png')
                        self.grid[row][col].setTexture(img)

    def surroundedByLand(self, row, col):
        if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile) and isinstance(self.grid[row - 1][col - 1], landTile) and isinstance(self.grid[row - 1][col + 1], landTile) and isinstance(self.grid[row + 1][col - 1], landTile) and isinstance(self.grid[row + 1][col + 1], landTile)):
            return True
        return False

    def checkTotalMountain(self):
        count = 0
        for row in range(30):
            for col in range(50):
                if isinstance(self.grid[row][col], mountainTile):
                    count += 1
        return count




    #Gives Proper Coastal Texture To All Land Tiles
    def fixCoastalTextures(self):
        for row in range(29):
            for col in range(49):
                if isinstance(self.grid[row][col], landTile):
                    if  (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col - 1], oceanTile) and isinstance(self.grid[row][col + 1], landTile)):                
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastL.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastT.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastB.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastTR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastBL.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastBR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastBR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastTL.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/Coast3B.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/Coast3T.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/Coast3L.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/Coast3R.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], oceanTile) and isinstance(self.grid[row + 1][col], oceanTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastPH.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], oceanTile) and isinstance(self.grid[row][col - 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastPV.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)
                    and isinstance(self.grid[row - 1][col - 1], landTile) and isinstance(self.grid[row - 1][col + 1], landTile) and isinstance(self.grid[row + 1][col - 1], oceanTile) and isinstance(self.grid[row + 1][col + 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastDBL.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)
                    and isinstance(self.grid[row - 1][col - 1], landTile) and isinstance(self.grid[row - 1][col + 1], landTile) and isinstance(self.grid[row + 1][col - 1], landTile) and isinstance(self.grid[row + 1][col + 1], oceanTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastDBR.png')
                        self.grid[row][col].setTexture(img)         
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)
                    and isinstance(self.grid[row - 1][col - 1], oceanTile) and isinstance(self.grid[row - 1][col + 1], landTile) and isinstance(self.grid[row + 1][col - 1], landTile) and isinstance(self.grid[row + 1][col + 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastDTL.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col + 1], landTile) and isinstance(self.grid[row][col - 1], landTile)
                    and isinstance(self.grid[row - 1][col - 1], landTile) and isinstance(self.grid[row - 1][col + 1], oceanTile) and isinstance(self.grid[row + 1][col - 1], landTile) and isinstance(self.grid[row + 1][col + 1], landTile)):
                        self.grid[row][col] = coastalTile(col*25, row*25, 25, 25)
                        img = pygame.image.load('Graphics/CoastDTR.png')
                        self.grid[row][col].setTexture(img)
                
    def fixMountainTextures(self):
        for row in range(29):
            for col in range(49):  
                if isinstance(self.grid[row][col], mountainTile):
                    if  (not isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile)):                
                        img = pygame.image.load('Graphics/MountainL.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainT.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainB.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainTR.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainBL.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainBR.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainTL.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile)):
                        img = pygame.image.load('Graphics/Mountain3B.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/Mountain3T.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/Mountain3L.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/Mountain3R.png')
                        self.grid[row][col].setTexture(img)
                    if (not isinstance(self.grid[row - 1][col], mountainTile) and not isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1],mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainH.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and not isinstance(self.grid[row][col + 1], mountainTile) and not isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainV.png')
                        self.grid[row][col].setTexture(img)
                    if (isinstance(self.grid[row - 1][col], mountainTile) and isinstance(self.grid[row + 1][col], mountainTile) and isinstance(self.grid[row][col + 1], mountainTile) and isinstance(self.grid[row][col - 1], mountainTile)):
                        img = pygame.image.load('Graphics/MountainA.png')
                        self.grid[row][col].setTexture(img)

    def istileowned(self, cordx, cordy, players, numplayers):
        tilex=cordx
        tiley=cordy
        tileid = self.grid[tiley][tilex].getID()
        #targettile= self.grid[tiley][tilex]
        for y in range (numplayers):
            for x in range (len(players[y].territories)):
                if (players[y].territories[x]==tileid):
                    return True 
        return False
                    

    #Develop Forest
    def CreateForest(self):
        foundLand = True
        row = random.randrange(1, 29)
        col = random.randrange(1, 49)
        while foundLand:
            if (isinstance(self.grid[row][col], landTile)):
                foundLand = False
            else:
                row = random.randrange(1, 29)
                col = random.randrange(1, 49) 
        while (isinstance(self.grid[row - 1][col], landTile) and isinstance(self.grid[row + 1][col], landTile) and isinstance(self.grid[row][col - 1], landTile) and isinstance(self.grid[row][col + 1], landTile)
        and row < 29 and col < 49 and isinstance(self.grid[row - 1][col - 1], landTile) and isinstance(self.grid[row + 1][col - 1], landTile) and isinstance(self.grid[row + 1][col + 1], landTile) and isinstance(self.grid[row - 1][col + 1], landTile)):    
            self.grid[row][col] = forestTile(col*25, row*25, 25, 25)
            choice = random.randrange(1, 5)
            if choice == 1:
                row -= 1
            elif choice == 2:
                row += 1
            elif choice == 3:
                col -= 1
            else:
                col += 1


    def createPlainsTiles(self):
        for row in range(30):
            for col in range(50):
                if isinstance(self.grid[row][col], landTile):
                    if not (isinstance(self.grid[row][col], coastalTile) or isinstance(self.grid[row][col], forestTile) or isinstance(self.grid[row][col], mountainTile)):
                        self.grid[row][col] = plainsTile(col * 25, row * 25, 25, 25)

    def giveTilesProduction(self):
        for row in range(30):
            for col in range(50):
                self.grid[row][col].setProduction()

    def fillWithOcean(self):
        for row in range(30):
            temp_row = []
            for col in range(50):
                x = col * 25
                y = row * 25
                temp_row.append(oceanTile(x, y, 25, 25))
            self.grid.append(temp_row)

    def buildMap(self):
        self.fillWithOcean()
        self.genLand(random.randrange(0, 50), random.randrange(0, 30))
        while not self.isValidGen(): 
            self.genLand(10, 5)
            if self.checkTotalLand() > 700:
                break
            self.genLand(10, 25)
            if self.checkTotalLand() > 700:
                break    
            self.genLand(45, 5)
            if self.checkTotalLand() > 700:
                break
            self.genLand(45, 25)
            if self.checkTotalLand() > 700:
                break
        x = 0
        count = 0
        for col in range(50):
            self.grid[0][count] = oceanTile(x, 0, 25, 25)
            x += 25
            count += 1
        x = 0
        count = 0
        for col in range(50):
            self.grid[29][count] = oceanTile(x, 725, 25, 25)
            x += 25
            count += 1
        y = 0
        count = 0
        for row in range(30):
            self.grid[count][0] = oceanTile(0, y, 25, 25)
            count += 1
            y += 25
        y = 0
        count = 0
        for row in range(30):
            self.grid[count][49] = oceanTile(1225, y, 25, 25)
            count += 1
            y += 25
        self.removeIsolatedOcean()
        #print(self.checkTotalLand())
        self.fixCoastalTextures()
        for a in range(75):
            self.CreateForest()
        while self.checkTotalMountain() < 60:
            self.CreateMountains()
        self.createPlainsTiles()
        self.randomizeTextures()
        self.fixMountainTextures()
        #Giving all Land Tiles an ID
        counter = -1
        for row in range(30):
            for col in range(50):
                    counter += 1
                    self.grid[row][col].setID(counter)
        self.giveTilesProduction()

    def displayMap(self, screen):
        for row in range(30):
            for col in range(50):
                self.grid[row][col].draw(screen)