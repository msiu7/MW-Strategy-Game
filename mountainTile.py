import pygame
from landTile import landTile
import random

class mountainTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/mountain.png')

    def setProduction(self):    
          self.stoneProduction = random.randint(1, 5)
          self.goldProduction = random.randint(1, 5)
          self.tileValue = (self.stoneProduction + self.goldProduction) * 5 
    
    def returnProduction1(self):
        return (f"Stone Production: {self.stoneProduction}")

    def returnProduction2(self):
        return (f"Gold Production: {self.goldProduction}")
    
    def returnStoneProduction(self):
        return self.stoneProduction
    
    def returnGoldProduction(self):
        return self.goldProduction 