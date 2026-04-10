from tile import tile
import pygame
import math
from population import population

class landTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/land.png')
        self.isCoastal = False
        self.populationperturn = 0
        self.directCoastalAdjacencyValue = 0b0
        self.diagonalCoastalAdjacencyValue = 0b0

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

    def upgradeTile(self, player):
        if self.level == 1 and player.getBrick() >= 50:
                player.subtractBrick(50)
                self.level += 1
        elif self.level == 2 and player.getBrick() >= 100:
                player.subtractBrick(100)
                self.level += 1

    def getCordsx(self):
        return (self.x)

    def getCordsy(self):
        return (self.y)
    
    def returnID(self):
        return self.ID
    
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
