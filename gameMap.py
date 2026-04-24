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
        self.relativePositionDict = { "TL" : 128,
        "TC" : 64,
        "TR" : 32,
        "L" : 16,
        "R" : 8,
        "BL" : 4,
        "BC" : 2,
        "BR" : 1
        } #based on binary (tbh not really necessary I just thought using a dictionary at some point would be nice)

    def setRelativePositionForOneTile(self, row, col):
        if (row == 0 or row == 29 or col == 0 or col == 49):
            return
        self.grid[row][col].relativePositionValue = 0
        if isinstance(self.grid[row - 1][col - 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["TL"]
        if isinstance(self.grid[row - 1][col], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["TC"]
        if isinstance(self.grid[row - 1][col + 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["TR"]
        if isinstance(self.grid[row][col - 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["L"]
        if isinstance(self.grid[row][col + 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["R"]
        if isinstance(self.grid[row + 1][col - 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["BL"]
        if isinstance(self.grid[row + 1][col], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["BC"]
        if isinstance(self.grid[row + 1][col + 1], landTile):
            self.grid[row][col].relativePositionValue += self.relativePositionDict["BR"]

    def setRelativePositionsForAllTiles(self):
        for row in range(1, 29):
            for col in range(1, 49):
                self.setRelativePositionForOneTile(row, col)

    def setFourBlockRelativePositionsForOneTile(self, row, col):
        if (row == 0 or row == 29 or col == 0 or col == 49):
            return
        self.grid[row][col].relativePositionTL = 0
        self.grid[row][col].relativePositionTR = 0
        self.grid[row][col].relativePositionBL = 0
        self.grid[row][col].relativePositionBR = 0
        if isinstance(self.grid[row][col], landTile):
            self.grid[row][col].relativePositionTL += 1  #(TL, TC, L, C) 8421
            self.grid[row][col].relativePositionTR += 2  #(TC, TR, C, R) 8421
            self.grid[row][col].relativePositionBL += 4  #(L, C, BL, BC) 8421
            self.grid[row][col].relativePositionBR += 8  #(C, R, BC, BR) 8421
        if isinstance(self.grid[row - 1][col - 1], landTile):
            self.grid[row][col].relativePositionTL += 8
        if isinstance(self.grid[row - 1][col], landTile):
            self.grid[row][col].relativePositionTL += 4
            self.grid[row][col].relativePositionTR += 8
        if isinstance(self.grid[row - 1][col + 1], landTile):
            self.grid[row][col].relativePositionTR += 4
        if isinstance(self.grid[row][col - 1], landTile):
            self.grid[row][col].relativePositionTL += 2
            self.grid[row][col].relativePositionBL += 8
        if isinstance(self.grid[row][col + 1], landTile):
            self.grid[row][col].relativePositionTR += 1
            self.grid[row][col].relativePositionBR += 8
        if isinstance(self.grid[row + 1][col - 1], landTile):
            self.grid[row][col].relativePositionBL += 2
        if isinstance(self.grid[row + 1][col], landTile):
            self.grid[row][col].relativePositionBL += 1
            self.grid[row][col].relativePositionBR += 2
        if isinstance(self.grid[row + 1][col + 1], landTile):
            self.grid[row][col].relativePositionBR += 1

    def setFourBlockRelativePositionsForAllTiles(self):
        for row in range(1, 29):
            for col in range(1, 49):
                self.setFourBlockRelativePositionsForOneTile(row, col)

    def eliminateDiagonalityForOneTile(self, row, col, countChanges):
        if isinstance(self.grid[row][col], landTile):
            if (self.grid[row][col].relativePositionTL == 9):
                self.grid[row - 1][col - 1] = oceanTile((col - 1) * 25, (row - 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row - 1, col - 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionTR == 6):
                self.grid[row - 1][col + 1] = oceanTile((col + 1) * 25, (row - 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row - 1, col + 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionBL == 6):
                self.grid[row + 1][col - 1] = oceanTile((col - 1) * 25, (row + 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row + 1, col - 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionBR == 9):
                self.grid[row + 1][col + 1] = oceanTile((col + 1) * 25, (row + 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row + 1, col + 1)
                countChanges += 1
        else:
            if (self.grid[row][col].relativePositionTL == 6):
                self.grid[row - 1][col - 1] = landTile((col - 1) * 25, (row - 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row - 1, col - 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionTR == 9):
                self.grid[row - 1][col + 1] = landTile((col + 1) * 25, (row - 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row - 1, col + 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionBL == 9):
                self.grid[row + 1][col - 1] = landTile((col - 1) * 25, (row + 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row + 1, col - 1)
                countChanges += 1
            if (self.grid[row][col].relativePositionBR == 6):
                self.grid[row + 1][col + 1] = landTile((col + 1) * 25, (row + 1) * 25, 25, 25)
                self.updateRelativePositionsForAllTilesAroundATile(row + 1, col + 1)
                countChanges += 1

    def eliminateDiagonalityForAllTiles(self, countChanges): #basically, land-to-land
        for row in range(1, 29):
            for col in range(1, 49):
                self.eliminateDiagonalityForOneTile(row, col, countChanges)

    def updateRelativePositionsForAllTilesAroundATile(self, row, col):
        for r in range (row - 1, row + 2):
            for c in range (col - 1, col + 2):
                self.setRelativePositionForOneTile(r, c)
                self.setFourBlockRelativePositionsForOneTile(r, c)

    def genLand(self, x, y):
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

    def removeCoastalAnomalies(self):
        countChanges = 1
        while(countChanges != 0):
            countChanges = 0
            self.setFourBlockRelativePositionsForAllTiles()
            self.eliminateDiagonalityForAllTiles(countChanges)
            self.setDirectCoastalAdjacencyValuesForAllTiles()
            self.setDiagonalCoastalAdjacencyValuesForAllTiles()
            for row in range(1, 29):
                for col in range(1, 49):
                    self.setDirectCoastalAdjacencyValuesForAllTiles()
                    self.setDiagonalCoastalAdjacencyValuesForAllTiles()
                    if isinstance(self.grid[row][col], landTile):
                        match self.grid[row][col].directCoastalAdjacencyValue:
                            case 0b0001:
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b0010:   
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b0100:
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b1000:
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b0110:
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b1001: 
                                self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                countChanges += 1
                            case 0b1111:
                                match self.grid[row][col].diagonalCoastalAdjacencyValue:
                                    case 0b1001:
                                        self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                        countChanges += 1
                                    case 0b0110:
                                        self.grid[row][col] = oceanTile(col * 25, row * 25, 25, 25)
                                        countChanges += 1
                                    case _:
                                        pass
                            case _:
                                pass
                    self.updateCoastalAdjacencyForAllTilesAroundATile(row, col)
                    self.updateRelativePositionsForAllTilesAroundATile(row, col)

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

    def createOceanBorder(self):
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

    def setDirectCoastalAdjacencyValuesForAllTiles(self):
        for row in range(29):
            for col in range(49):
                self.setDirectCoastalAdjacencyValuesForOneTile(row, col)

    def setDiagonalCoastalAdjacencyValuesForAllTiles(self):
        for row in range(29):
            for col in range(49):
                self.setDiagonalCoastalAdjacencyValuesForOneTile(row, col)

    def setDirectCoastalAdjacencyValuesForOneTile(self, row, col):
        if isinstance(self.grid[row][col], landTile):
            self.grid[row][col].directCoastalAdjacencyValue = 0
            if isinstance(self.grid[row + 1][col], landTile):
                self.grid[row][col].directCoastalAdjacencyValue |= (1 << 0)
            if isinstance(self.grid[row][col + 1], landTile):
                self.grid[row][col].directCoastalAdjacencyValue |= (1 << 1)
            if isinstance(self.grid[row][col - 1], landTile):
                self.grid[row][col].directCoastalAdjacencyValue |= (1 << 2)
            if isinstance(self.grid[row - 1][col], landTile):
                self.grid[row][col].directCoastalAdjacencyValue |= (1 << 3)
            #print(f"bit image: {self.grid[row][col].directCoastalAdjacencyValue}") #converts to int, but whatever
    '''
    { _ A _ }
    { B X C } tile.directCoastalAdjacencyValues = ABCD, X is the tile, 1 means land, 0 means ocean
    { _ D _ }
    '''

    def setDiagonalCoastalAdjacencyValuesForOneTile(self, row, col):
        if isinstance(self.grid[row][col], landTile):
            self.grid[row][col].diagonalCoastalAdjacencyValue = 0
            if isinstance(self.grid[row + 1][col + 1], landTile):
                self.grid[row][col].diagonalCoastalAdjacencyValue |= (1 << 0)
            if isinstance(self.grid[row + 1][col - 1], landTile):
                self.grid[row][col].diagonalCoastalAdjacencyValue |= (1 << 1)
            if isinstance(self.grid[row - 1][col + 1], landTile):
                self.grid[row][col].diagonalCoastalAdjacencyValue |= (1 << 2)
            if isinstance(self.grid[row - 1][col - 1], landTile):
                self.grid[row][col].diagonalCoastalAdjacencyValue |= (1 << 3)
                
    '''
    { A _ B }
    { _ X _ } tile.diagonalCoastalAdjacencyValues = ABCD, X is the tile, 1 means land, 0 means ocean
    { C _ D }
    '''
    def updateCoastalAdjacencyForAllTilesAroundATile(self, row, col):
        for r in range (row - 1, row + 2):
            for c in range (col - 1, col + 2):
                self.setDirectCoastalAdjacencyValuesForOneTile(r, c)
                self.setDiagonalCoastalAdjacencyValuesForOneTile(r, c)
                

    #Gives Proper Coastal Texture To All Land Tiles
    def fixCoastalTextures(self):
        for row in range(29):
            for col in range(49):
                if isinstance(self.grid[row][col], landTile):
                    match self.grid[row][col].directCoastalAdjacencyValue:
                        case 0b0001:  
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0001.png')
                        case 0b0010:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0010.png')
                        case 0b0011:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0011.png')
                        case 0b0100:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0100.png')
                        case 0b0101:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0101.png')
                        case 0b0110:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0110.png')
                        case 0b0111:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C0111.png')
                        case 0b1000:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1000.png')
                        case 0b1001:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1001.png')
                        case 0b1010:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1010.png')
                        case 0b1011:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1011.png')
                        case 0b1100:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1100.png')
                        case 0b1101:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1101.png')
                        case 0b1110:
                            self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                            img = pygame.image.load('Graphics/C1110.png')
                        case 0b1111:
                            match self.grid[row][col].diagonalCoastalAdjacencyValue:
                                # a good few of these never actually happen 
                                case 0b0111:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD0111.png')
                                case 0b1011:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD1011.png')
                                case 0b1101:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD1101.png')
                                case 0b1110:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD1110.png')
                                case 0b0011:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD0011.png')
                                case 0b1010:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD1010.png')
                                case 0b1100:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD1100.png')
                                case 0b0101:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/CD0101.png')
                                case 0b1111:
                                    img = pygame.image.load('Graphics/land.png')
                                case _:
                                    self.grid[row][col] = coastalTile(col * 25, row * 25, 25, 25)
                                    img = pygame.image.load('Graphics/red.png')
                        case _:
                            img = pygame.image.load('Graphics/filler.png')
                else:
                    img = pygame.image.load('Graphics/ocean.png')
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
            print("numgenerate")
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
        self.createOceanBorder()
        self.removeIsolatedOcean()
        self.removeCoastalAnomalies()
        self.setDirectCoastalAdjacencyValuesForAllTiles()
        self.setDiagonalCoastalAdjacencyValuesForAllTiles()
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