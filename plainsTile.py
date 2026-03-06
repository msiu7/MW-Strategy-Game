import pygame
from landTile import landTile
import random

class plainsTile(landTile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/land.png')
        
    def setProduction(self):    
        self.foodProduction = random.randint(1, 10)
        self.tileValue = (self.foodProduction) * 5
    
    def returnProduction1(self):
        return (f"Food Production: {self.foodProduction}")
    
    def returnProduction2(self):
        return (f"")
    
    def returnFoodProduction(self):
        return self.foodProduction