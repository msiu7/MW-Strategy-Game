import pygame
import random
from array import *
from population import *
from landTile import landTile
from oceanTile import oceanTile
from mountainTile import mountainTile
from forestTile import forestTile
from coastalTile import coastalTile
from plainsTile import plainsTile

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
        self.goldperturn = 0
        self.woodperturn = 0
        self.stoneperturn = 0
        self.foodperturn = 0
        self.brickperturn = 0
        self.gold = 1000
        self.wood = 100
        self.stone = 100
        self.food = 0
        self.brick = 100
        self.foodConsumption = 0

        #Spelunking/Treasure Hunting Variables
        self.lastTurnGoldFromTreasure = 0
        self.lastTurnBrickFromTreasure = 0 
        self.lastTurnFoodFromTreasure = 0 
        self.lastTurnStoneFromTreasure = 0
        self.lastTurnWoodFromTreasure = 0

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
        for a in range(0, len(self.territories)):
            for b in range(0, len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population)):   
                self.population.append(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population[b])                  

    def updatePopulation(self, grid):
        count = 0
        for a in range(0, len(self.territories)):
            if(isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50], landTile)):
                grid[(self.territories[a]) // 50][(self.territories[a]) % 50].updatePopulationPerTurn(self)  
        for a in range(0, len(self.territories)):
            if(isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50], landTile)):
                grid[(self.territories[a]) // 50][(self.territories[a]) % 50].autoAddPopulation()
                count += len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population)
        if count == 0 and len(self.territories) > 0:
            b = 0
            #while loop checks if b is an oceanTile, keeps running until territories[b] is a landTile
            while isinstance(grid[(self.territories[b]) // 50][(self.territories[b]) % 50], oceanTile):
                b = random.randint(0, len(self.territories)-1)
            grid[(self.territories[b]) // 50][(self.territories[b]) % 50].manuallyAddPopulation(1)
        numzero = 0
        numpos = 0  
        zero = []
        for a in range(len(self.territories)):
            if (len(grid[(self.territories[a]) // 50][(self.territories[a]) % 50].population) == 0) and (isinstance(grid[(self.territories[a]) // 50][(self.territories[a]) % 50], landTile)):
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
    
    def checkAdjacencyForMovement(self, id1, id2):
        if(self.doesTileBelongToPlayer(id1) and self.doesTileBelongToPlayer(id2)):
            if (id1 == id2 - 1):
                return True
            elif (id1 == id2 + 1):
                return True
            elif (id1 == id2 - 50):
                return True
            elif (id1 == id2 + 50):
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