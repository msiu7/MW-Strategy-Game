import population

class tile:
    
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.ID = 0
        self.width = width
        self.height = height
        self.tileValue = 0
        self.population = []
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
        self.spelunkingChance = 0
        self.functionalSpelunkingChance = 0
        self.spelunkingCooldown = 0
        self.level = 1

    def updateFunctionalProduction(self):
        self.functionalWoodProduction = self.woodProduction * self.getCivLength() * (2**(self.level-1))
        self.functionalBrickProduction = self.brickProduction * self.getCivLength() * (2**(self.level-1))
        self.functionalGoldProduction = self.goldProduction * self.getCivLength() * (2**(self.level-1))
        self.functionalStoneProduction = self.stoneProduction * self.getCivLength() * (2**(self.level-1))
        self.functionalFoodProduction = self.foodProduction * self.getCivLength() * (2**(self.level-1))
        self.functionalSpelunkingChance = self.spelunkingChance * self.getCivLength() * (2**(self.level-1))

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

    def popToNewType(self, index, newtype):
        population[index].changeType(newtype)  

    def getCivLength(self):
        count = 0
        for a in range(len(self.population)):
            if self.population[a].type == "civilian":
                count += 1
        return count

    def getSolLength(self):
        count = 0
        for a in range(len(self.population)):
            if self.population[a].type == "soldier":
                count += 1
        return count
    
    def getUnemployedLength(self):
        count = 0
        for a in range(len(self.population)):
            if self.population[a].type == "unemployed":
                count += 1
        return count 
    
    def findIndexOfType(self, type):
        for a in range(len(self.population)):
            if self.population[a].type == type:
                return a
        return -1
    