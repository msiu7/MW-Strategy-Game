from tile import tile
import pygame
import random

class oceanTile(tile):
    
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/ocean.png')
    
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def setProduction(self):    
        self.spelunkingChance = random.randint(1, 10)
        self.tileValue = (self.spelunkingChance) * 5

    def returnProduction1(self):
        return (f"Treasure Chance: {self.spelunkingChance}")
    
    def returnProduction2(self):
        return (f"")
    
    def getCordsx(self):
        return (self.x)
    
    def getCordsy(self):
      return (self.y)