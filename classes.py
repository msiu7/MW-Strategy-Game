import pygame
import random
from array import *
import math

class population:

    def __init__ (self, tilerow, tilecol):
        self.type = "unemployed"
        self.tilerow = tilerow
        self.tilecol = tilecol
    
    def movePopulation(self, tilerow1, tilecol1, tilerow2, tilecol2, grid):
        grid[tilerow2][tilecol2].population.append(grid[tilerow1][tilecol1].population[len(grid[tilerow1][tilecol1].population)-1])
        grid[tilerow1][tilecol1].population.remove(grid[tilerow1][tilecol1].population[len(grid[tilerow1][tilecol1].population)-1])
        grid[tilerow2][tilecol2].population[len(grid[tilerow2][tilecol2].population)].tilerow = tilerow2
        grid[tilerow2][tilecol2].population[len(grid[tilerow2][tilecol2].population)].tilecol = tilecol2
        
class civilian(population):

    def __init__ (self, tilerow, tilecol):
        super().__init__(tilerow, tilecol)
        self.type = "civilian"
        self.tilerow = tilerow
        self.tilecol = tilecol

class farmer(civilian):

    def __init__ (self, tilerow, tilecol):
        super().__init__(tilerow, tilecol)
        self.type = "farmer"

class soldier(population):

    def __init__(self, tilerow, tilecol):
        
        super().__init__(tilerow, tilecol)
        self.type = "soldier"
        self.tilerow = tilerow
        self.tilecol = tilecol

class war (population):
    def __init__(self):
        super().__init__(self)
        self.atwar = False
        self.selection = False
        self.xy = 0
        

    def warselection(self):
        self.selection = True
        while self.selection == True:
          self.xy = event.pos()
        
    def warbegin(self):
        self.atwar = True
        
        



#Base Superclass
class tile:
    
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.ID = 0
        self.width = width
        self.height = height
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def setID(self, x):
        self.ID = x
        
    def getID(self):
        return self.ID

    def getRow(self):
        row = (self.ID // 50) 
        return row
    
    def getCol(self):
        col = (self.ID) % 50 
        return col

    def setTexture(self, texture):
        self.image = texture
    
#Subclass Land Tile 
class landTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')
        self.isCoastal = False
        self.tileValue = 0
        self.brickProduction = 0
        self.foodProduction = 0
        self.goldProduction = 0
        self.stoneProduction = 0
        self.woodProduction = 0
        self.functionalWoodProduction = 0
        self.functionalBrickProduction = 0
        self.functionalGoldProduction = 0
        self.functionalStoneProduction = 0 
        self.functionalFoodProduction = 0
        self.populationperturn = 0
        self.population = []
        self.civilians = []
        self.soldiers = []

    def popToSoldier(self, index, row, col):
        self.population[index] = soldier(row, col)
        self.soldiers.append(self.population[index])     

    def popToCivilian(self, index, row, col):
        self.population[index] = civilian(row, col)
        self.civilians.append(self.population[index])

    def civToSoldier(self, index, row, col):
        self.civilians[index] = soldier(row, col)
        self.soldiers.append(self.civilians[index])
        self.civilians.pop(index)

    def solToCivilian(self, index, row, col):
        self.soldiers[index] = civilian(row, col)
        self.civilians.append(self.soldiers[index])
        self.soldiers.pop(index)

    
    
    def updatePopulationPerTurn(self, player):

            
        nextturnfood = player.food + player.foodperturn - player.foodConsumption
        if player.food > 0 and nextturnfood > 0: 
            self.populationperturn = nextturnfood / player.food
            
        elif player.food == 0 and nextturnfood != 0:
            if nextturnfood > 0:
                self.populationperturn = 0
                
            else: 
                self.populationperturn = -1
                
        elif player.food != 0 and nextturnfood == 0:
            self.populationperturn = 0
            
        elif player.food != 0 and nextturnfood < 0:
            self.populationperturn = -1
            
        else: 
            populationperturn = 0
            
        print(f"pop:{self.population} && popperturn:{self.populationperturn} && {player.foodConsumption} && {nextturnfood}")
    
    def updateFunctionalProduction(self):
        self.functionalWoodProduction = self.woodProduction * len(self.population)
        self.functionalBrickProduction = self.brickProduction * len(self.population)
        self.functionalGoldProduction = self.goldProduction * len(self.population)
        self.functionalStoneProduction = self.stoneProduction * len(self.population)
        self.functionalFoodProduction = self.foodProduction * len(self.population)

    def getCordsx(self):
        return (self.x)

    def getCordsy(self):
        return (self.y)
    
    def returnID(self):
        return self.ID

    def returnValue(self):
        return self.tileValue
    
    def manuallyAddPopulation(self, numpop):
        numtrnc = math.trunc(numpop)
        for a in range(numtrnc):
            self.population.append(population(self.getRow, self.getCol))
        
    def autoAddPopulation(self):
        ppttrnc = math.trunc(self.populationperturn)
        if ppttrnc > 0:
            for a in range(ppttrnc):
                self.population.append(population(self.getRow, self.getCol))
        elif ppttrnc < 0:
            for a in range(abs(ppttrnc)):
                self.population.remove(self.population[len(self.population)-1])

    def getPopulation(self):
        return self.population

class plainsTile(landTile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')
        
    def setProduction(self):    
        self.foodProduction = random.randint(1, 10)
        self.tileValue = (self.foodProduction) * 5

    def returnValue(self):
        return self.tileValue  
    
    def returnProduction1(self):
        return (f"Food Production: {self.foodProduction}")
    
    def returnProduction2(self):
        return (f"")
    
    def returnFoodProduction(self):
        return self.foodProduction

class coastalTile(landTile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')

    def setProduction(self):
        self.brickProduction = random.randint(1, 5)
        self.foodProduction = random.randint(1, 5)
        self.tileValue = (self.brickProduction + self.foodProduction) * 5

    def returnProduction1(self):
        return (f"Brick Production: {self.brickProduction}")

    def returnProduction2(self):
        return (f"Food Production: {self.foodProduction}")

    def returnValue(self):
        return self.tileValue
    
    def returnFoodProduction(self):
        return self.foodProduction
    
    def returnBrickProduction(self):
        return self.brickProduction

class mountainTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('mountain.png')

    def setProduction(self):    
          self.stoneProduction = random.randint(1, 5)
          self.goldProduction = random.randint(1, 5)
          self.tileValue = (self.stoneProduction + self.goldProduction) * 5

    def returnValue(self):
        return self.tileValue  
    
    def returnProduction1(self):
        return (f"Stone Production: {self.stoneProduction}")

    def returnProduction2(self):
        return (f"Gold Production: {self.goldProduction}")
    
    def returnStoneProduction(self):
        return self.stoneProduction
    
    def returnGoldProduction(self):
        return self.goldProduction 

class forestTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('forest.png')

    def setProduction(self):  
          self.woodProduction = random.randint(1, 5)
          self.foodProduction = random.randint(1, 5)
          self.tileValue = (self.woodProduction + self.foodProduction) * 5

    def returnValue(self):
        return self.tileValue  

    def returnProduction1(self):
        return (f"Wood Production: {self.woodProduction}")
    
    def returnProduction2(self):
        return (f"Food Production: {self.foodProduction}")

    def returnFoodProduction(self):
        return self.foodProduction

    def returnWoodProduction(self):
        return self.woodProduction

#Subclass Ocean Tile
class oceanTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('ocean.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    
    def getCordsx(self):
        return (self.x)
    
    def getCordsy(self):
      return (self.y)

#Creates Unique Player
class player:
    def __init__(self, name, color):
        self.territories = []
        self.name = name
        self.color = color
        self.borderingTerritories = []
        
        
        
        if color == '1':
            self.rgb = (255, 18, 5)
        if color == '2': 
            self.rgb = (165, 168, 0)
        if color == '3': 
            self.rgb = (3, 168, 0)
        if color == '4':
            self.rgb = (0, 25, 168)
        if color == '5':
            self.rgb = (0, 0, 0)
        if color == '6':
           self.rgb = (0, 168, 157)
        

        

        
        #Game mechanics related variables
        self.population = []
        self.civilians = []
        self.soldiers = []
        self.goldperturn = 0
        self.woodperturn = 0
        self.stoneperturn = 0
        self.foodperturn = 0
        self.brickperturn = 0
        self.gold = 1000
        self.wood = 0
        self.stone = 0
        self.food = 0
        self.brick = 0
        self.foodConsumption = 0
        

    def updateFoodConsumption(self):
        self.foodConsumption = len(self.population) * 4

    def consumeFood(self):
        self.updateFoodConsumption()
        self.food -= self.foodConsumption
        if self.food < 0:
            self.food = 0
    
    def updateFunctionalProductionValues(self, grid):
        count0 = 0
        count1 = 0
        for a in range(0, len(self.territories)):
            grid[(self.territories[a]) // 50][(self.territories[a]) % 50].updateFunctionalProduction()
            count0 += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalFoodProduction
            print(f"functional: {count0}")
            count1 += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].foodProduction
            print(f"regular: {count1}")

    def updateProductionValues(self, grid):
        self.woodperturn = 0
        self.stoneperturn = 0
        self.goldperturn = 0
        self.foodperturn = 0
        self.brickperturn = 0
        for a in range(0, len(self.territories)):
            if (isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50], forestTile)):
                self.woodperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalWoodProduction
                self.foodperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalFoodProduction
            if (isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50], mountainTile)):
                self.stoneperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalStoneProduction
                self.goldperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalGoldProduction
            if (isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50 ], coastalTile)):
                self.brickperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalBrickProduction
                self.foodperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalFoodProduction
            if (isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50 ], plainsTile)):
                self.foodperturn += grid[(self.territories[a]) // 50][(self.territories[a]) % 50].functionalFoodProduction

    def totalPlayerPopulation(self, grid):
        self.population = []
        self.civilians = []
        self.soldiers = []
        for a in range(0, len(self.territories)):
            for b in range(0, len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population)):   
                self.population.append(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b])
                if grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b].type == "civilian":
                    self.civilians.append(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b])
                if grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b].type == "soldier":
                    self.soldiers.append(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b])
                    

    def updatePopulation(self, grid):
        count = 0
        for a in range(0, len(self.territories)):
            grid[(self.territories[a]) // 50][(self.territories[a]) % 50].updatePopulationPerTurn(self)  
        for a in range(0, len(self.territories)):
            grid[(self.territories[a]) // 50][(self.territories[a]) % 50].autoAddPopulation()
            count += len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population)
        if count == 0 and len(self.territories) > 0:
            b = random.randint(0, len(self.territories)-1)
            grid[(self.territories[b]) // 50][(self.territories[b]) % 50].manuallyAddPopulation(1)
        numzero = 0
        numpos = 0  
        zero = []
        for a in range(len(self.territories)):
            if (len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population) == 0):
                numzero += 1
                zero.append(self.territories[a])
            else:
                numpos += 1
        if numpos > 0:
            for a in range(len(zero)):
                self.subtractTerritoryFromPlayer(zero[a])
        else:
            for a in range(len(zero)-1):
                self.subtractTerritoryFromPlayer(zero[a])
                self.territories[0].manuallyAddPopulation(1)

            

        #print(f"Numzero: {numzero}, Numpos: {numpos}")
                #self.subtractTerritoryFromPlayer(self.territories[a])
                #a-=1
                #print(f"a value:{a}")




   

    def addProductionToTotal(self):
        self.gold += self.goldperturn
        self.wood += self.woodperturn
        self.stone += self.stoneperturn 
        self.food += self.foodperturn
        self.brick += self.brickperturn 
    
    def addTerritoryToPlayer(self, id):
        self.territories.append(id)

    def subtractTerritoryFromPlayer(self, id):
        if len(self.territories) > 1:
            self.territories.remove(id)
        #print(len(self.territories))

    def returnNumTerritories(self):
        return len(self.territories)

    def doesTileBelongToPlayer(self, id):
        for a in range(0, len(self.territories)):
            if id == self.territories[a]:
                return True
        return False

    def checkExpandable(self, id, grid):
        if len(self.territories) == 0:
            return True    
        for a in range(0, len(self.borderingTerritories)):       
            if (self.borderingTerritories[a] == id - 1):
                return True
            elif (self.borderingTerritories[a] == id + 1):
                return True
            elif (self.borderingTerritories[a] == id - 50):
                return True
            elif (self.borderingTerritories[a] == id + 50):
                return True
        return False

    def addBordering(self):
        self.borderingTerritories = []
        a = len(self.territories)
        b = 0
        while (b < a):

            c = self.territories[b]
            if not (self.doesTileBelongToPlayer(c - 1) and self.doesTileBelongToPlayer(c + 1) and self.doesTileBelongToPlayer(c - 50) and self.doesTileBelongToPlayer(c + 50)):
                self.borderingTerritories.append(c)
            b += 1
                

    def drawBorders(self, screen):
        
        for a in range(0, len(self.borderingTerritories)):
            #SurFued
            if ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen,(self.rgb), top) 
                pygame.draw.rect(screen, (self.rgb), bottom)
                pygame.draw.rect(screen,(self.rgb), left)  
            
            
            # left, top, right
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen, (self.rgb), top)
                pygame.draw.rect(screen, (self.rgb), left)

            # left, bottom, right
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen, (self.rgb), bottom)
                pygame.draw.rect(screen, (self.rgb), left)
                
            # top, bottom, right
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), top)
                pygame.draw.rect(screen, (self.rgb), bottom)
                pygame.draw.rect(screen, (self.rgb), right)

            # top, bottom, left
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), top)
                pygame.draw.rect(screen, (self.rgb), bottom)
                pygame.draw.rect(screen, (self.rgb), left)
            
            
            # right, top
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen, (self.rgb), top)
            

            # left, top
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                pygame.draw.rect(screen, (self.rgb), left)
                pygame.draw.rect(screen, (self.rgb), top)
                
            # left, bottom
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                pygame.draw.rect(screen, (self.rgb), left)
                pygame.draw.rect(screen, (self.rgb), bottom)       

            # right, bottom
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen, (self.rgb), bottom)

            # top, bottom
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                pygame.draw.rect(screen, (self.rgb), top)
                pygame.draw.rect(screen, (self.rgb), bottom)
                
            # left, right
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), left)
                pygame.draw.rect(screen, (self.rgb), right)

            # left
            elif ((not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                left = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), left)
            
            # right
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 23, (self.borderingTerritories[a] // 50) * 25, 2, 25)
                pygame.draw.rect(screen, (self.rgb), right)
            
            # top
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 2)
                pygame.draw.rect(screen, (self.rgb), top)

            # bottom
            elif ((self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1)) and (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50)) and (not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50))):
                #width,height
                bottom = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25 + 23, 25, 2)
                pygame.draw.rect(screen, (self.rgb), bottom)



      
    def getGold(self):
        return self.gold
    
    def subtractGold(self, amount):
        self.gold -= amount
    
    def getWood(self):
        return self.wood

    def subtractWood(self, amount):
        self.wood -= amount

    def getStone(self):
        return self.stone
    
    def subtractStone(self, amount):
        self.stone -= amount
        
    def getFood(self):
        return self.food
    
    def subtractFood(self, amount):
        self.food -= amount
    
    def getBrick(self):
        return self.brick
    
    def subtractBrick(self, amount):
        self.brick -= amount
        
    def getFoodConsumption(self):
        return self.foodConsumption
    
    def endTurnSequence(self, grid):
        self.totalPlayerPopulation(grid)
        self.updateFunctionalProductionValues(grid)
        self.updateProductionValues(grid)
        self.updateFoodConsumption()           
        self.updatePopulation(grid)
        self.addProductionToTotal()           
        self.consumeFood()
        self.totalPlayerPopulation(grid)
        self.updateFunctionalProductionValues(grid)
        self.updateProductionValues(grid)
        self.updateFoodConsumption()
        print(self.foodperturn)
        print(f"Total Player Population: {len(self.population)}")
        for a in range(len(self.population)):
            print(self.population[a])

#class diplomacy:
 #   def __init__(self)
    
#class opinion(diplomacy):
#   def __init__(self, )
#        self.opinion = 0
