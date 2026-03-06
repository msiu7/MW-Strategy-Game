import pygame
from landTile import landTile
import random

class forestTile(landTile):

    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/forest.png')

    def setProduction(self):  
          self.woodProduction = random.randint(1, 5)
          self.foodProduction = random.randint(1, 5)
          self.tileValue = (self.woodProduction + self.foodProduction) * 5

    def returnProduction1(self):
        return (f"Wood Production: {self.woodProduction}")
    
    def returnProduction2(self):
        return (f"Food Production: {self.foodProduction}")

    def returnFoodProduction(self):
        return self.foodProduction

    def returnWoodProduction(self):
        return self.woodProduction