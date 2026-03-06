import pygame
from landTile import landTile
import random

class coastalTile(landTile):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.image = pygame.image.load('Graphics/land.png')

    def setProduction(self):
        self.brickProduction = random.randint(1, 5)
        self.foodProduction = random.randint(1, 5)
        self.tileValue = (self.brickProduction + self.foodProduction) * 5

    def returnProduction1(self):
        return (f"Brick Production: {self.brickProduction}")

    def returnProduction2(self):
        return (f"Food Production: {self.foodProduction}")
    
    def returnFoodProduction(self):
        return self.foodProduction
    
    def returnBrickProduction(self):
        return self.brickProduction