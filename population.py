class population:

    def __init__ (self, tilerow, tilecol):
        self.type = "unemployed"
        self.tilerow = tilerow
        self.tilecol = tilecol
        #type list: "unemployed", "civilian", "soldier"

        #population score (maybe we should do different scores for each type?)
        self.score = 1
    
    def movePopulation(self, index, tilerow1, tilecol1, tilerow2, tilecol2, grid):
        grid[tilerow2][tilecol2].population.append(self)
        grid[tilerow1][tilecol1].population.pop(index)
        self.tilerow = tilerow2
        self.tilecol = tilecol2

    def changeType(self, newtype):
        self.type = newtype
