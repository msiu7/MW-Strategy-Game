import pygame
import random
from array import *

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
        row = (self.ID - 1) // 50
        return row
    
    def getCol(self):
        col = (self.ID - 1) % 50
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

    def getCordsx(self):
        return (self.x)

    def getCordsy(self):
        return (self.y)
    
    def returnID(self):
        return self.ID

    def returnValue(self):
        return self.tileValue

class plainsTile(landTile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')
        self.foodProduction = 0
        

    def setProduction(self):    
        self.foodProduction = random.randint(1, 10)
        self.tileValue = (self.foodProduction) * 10

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
        self.foodProduction = 0
        self.brickProduction = 0 
    
    def setProduction(self):
        self.brickProduction = random.randint(1, 5)
        self.foodProduction = random.randint(1, 5)
        self.tileValue = (self.brickProduction + self.foodProduction) * 10

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
        self.stoneProduction = 0
        self.goldProduction = 0

    def setProduction(self):    
          self.stoneProduction = random.randint(1, 5)
          self.goldProduction = random.randint(1, 5)
          self.tileValue = (self.stoneProduction + self.goldProduction) * 10

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

    # def setProduction(self, newProduction):
   
        

class forestTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('forest.png')
        self.woodProduction = 0
        self.foodProduction = 0

    def setProduction(self):  
          self.woodProduction = random.randint(1, 5)
          self.foodProduction = random.randint(1, 5)
          self.tileValue = (self.woodProduction + self.foodProduction) * 10

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

    # def setProduction(self, newProduction):
  


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
        self.population = 0
        self.army = 0
        self.goldperturn = 0
        self.woodperturn = 0
        self.stoneperturn = 0
        self.foodperturn = 0
        self.brickperturn = 0
        self.gold = 0
        self.wood = 0
        self.stone = 0
        self.food = 0
        self.brick = 0



    def updateProductionValues(self, grid):
        for a in range(0, len(self.territories)):
            if (isinstance(grid[self.territories[a].getRow()][self.territories[a].getCol()], forestTile)):
                self.woodperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnWoodProduction()
                self.foodperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnFoodProduction()
            if (isinstance(grid[self.territories[a].getRow()][self.territories[a].getCol()], mountainTile)):
                self.stoneperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnStoneProduction()
                self.goldperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnGoldProduction()
            if (isinstance(grid[self.territories[a].getRow()][self.territories[a].getCol()], coastalTile)):
                self.brickperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnBrickProduction()
                self.foodperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnFoodProduction()
            if (isinstance(grid[self.territories[a].getRow()][self.territories[a].getCol()], plainsTile)):
                self.foodperturn += grid[self.territories[a].getRow()][self.territories[a].getCol()].returnFoodProduction()

    def addProductionToTotal(self):
        self.gold += self.goldperturn
        self.wood += self.woodperturn
        self.stone += self.stoneperturn 
        self.food += self.foodperturn
        self.brick += self.brickperturn 
    
    def addTerritoryToPlayer(self, id):
        self.territories.append(id)

    def doesTileBelongToPlayer(self, id):
        for a in range(0, len(self.territories)):
            if id == self.territories[a]:
                return True
        return False

    def checkExpandable(self, id, grid):
        if (self.doesTileBelongToPlayer(grid[(self.getRow(id))-1][self.getCol(id)].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[(self.getRow(id))+1][self.getCol(id)].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[self.getRow(id)][(self.getCol(id))-1].getID())):
            return True
        if (self.doesTileBelongToPlayer(grid[self.getRow(id)][(self.getCol(id))+1].getID())):
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
            #Surrounded
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
        
  