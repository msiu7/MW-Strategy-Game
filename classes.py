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

    def getRow(self, id):
        row = (id - 1) // 50
        return row
    
    def getCol(self, id):
        col = (id - 1) % 50
        return col

    def setTexture(self, texture):
        self.image = texture
    
#Subclass Land Tile 
class landTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('land.png')
    
    def getCordsx(self):
        return (self.x)

    def getCordsy(self):
        return (self.y)
    
    def returnID(self):
        return self.ID

    def setCoastal(self):
        self.isCoastal = True
        self.brickProduction = 0
        
    def checkIfCoastal(self):
        if isCoastal:
            return True
        return False

class mountainTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('mountain.png')
        self.stoneProduction = 0
        self.goldProduction = 0

    #def setProduction(self):
    #    if checkIfCoastal = true:
    #       self.brickProduction = random.randint(1, 10)    
    #       self.stoneProduction = random.randint(1, 5)
    #       self.goldProduction = random.randint(1, 5)
    #       self.tileValue += (brickProduction + stoneProduction + goldProduction) * 10

    # def returnValue(self)
    #     return self.tileValue  
    
        

    # def setProduction(self, newProduction):
   
        

class forestTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('forest.png')
        self.woodProduction = 0
        self.foodProduction = 0

    #def setProduction(self):
    #    if checkIfCoastal = true:
    #       self.brickProduction = random.randint(1, 10)    
    #       self.stoneProduction = random.randint(1, 5)
    #       self.goldProduction = random.randint(1, 5)
    #       self.tileValue += (brickProduction + stoneProduction + goldProduction) * 10

    # def returnValue(self)
    #     return self.tileValue  

        

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
        self.gold = 0
        self.wood = 0
        self.stone = 0
        self.food = 0

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
        while (b < a - 1):

            c = self.territories[b]
            if not (self.doesTileBelongToPlayer(c - 1) and self.doesTileBelongToPlayer(c + 1) and self.doesTileBelongToPlayer(c - 50) and self.doesTileBelongToPlayer(c + 50)):
                self.borderingTerritories.append(c)
            b += 1
                

    def drawBorders(self, screen):
        
        for a in range(0, len(self.borderingTerritories)):
            #for bordering right and top unowned tiles
             
            if (self.doesTileBelongToPlayer(self.borderingTerritories[a] - 1) and not self.doesTileBelongToPlayer(self.borderingTerritories[a] + 1) and not self.doesTileBelongToPlayer(self.borderingTerritories[a] - 50) and self.doesTileBelongToPlayer(self.borderingTerritories[a] + 50)):
                #width,height
                right = pygame.Rect((self.borderingTerritories[a] % 50) * 25 + 20, (self.borderingTerritories[a] // 50) * 25, 5, 25)
                top = pygame.Rect((self.borderingTerritories[a] % 50) * 25, (self.borderingTerritories[a] // 50) * 25, 25, 5)
                pygame.draw.rect(screen, (self.rgb), right)
                pygame.draw.rect(screen,(self.rgb),top)
                
                
            
    #         #if 
            
    #         if (not self.doesTileBelongToPlayer((self.borderingTerritories[a]) + 1) and not self.doesTileBelongToPlayer((self.borderingTerritories[a]) - 50) ):
    #            rectangleeewangle = 
               
               
    #            #code to set texture

    #         #for bordering right and bottom unowned tiles   
    #         if (not self.doesTileBelongToPlayer((self.borderingTerritories[a]) + 1) and not self.doesTileBelongToPlayer((self.borderingTerritories[a]) + 50)):
    #             #code to set texture
            
    #         #for bordering left and top unowned tiles 
    #         if (not self.doesTileBelongToPlayer((self.borderingTerritories[a]) - 1) and not self.doesTileBelongToPlayer((self.borderingTerritories[a]) - 50)):    
    #             #code to set texture
            
    #         #for bordering left and bottom unowned tile
    #         if (not self.doesTileBelongToPlayer((self.borderingTerritories[a]) - 1) and not self.doesTileBelongToPlayer((self.borderingTerritories[a]) + 50)):
    #             #code to set texture
      
    #         if (not self.doesTileBelongToPlayer((self.borderingTerritories[a]) - 1) and not self.doesTileBelongToPlayer((self.borderingTerritories[a]) + 50) and ):
    #             #code to set texture
            
      

        
   