import pygame
from player import player
#Player and Territory Management
usedIDs = []
players = []
currentplayerindex = 0
turnnumber = 1

#Setting up Initial Player Screen
pygame.init() 
Background_color = (48, 55, 191)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 850
text = pygame.font.SysFont("Arial", 30)
text1 = pygame.font.SysFont("Arial", 45)
text2 = pygame.font.SysFont("Arial", 45)
text3 = pygame.font.SysFont("Arial", 10)
screen0 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen0.fill(Background_color)
rect2 = pygame.Rect(200, 200, 100, 100)
rect3 = pygame.Rect(625, 200, 100, 100)
rect4 = pygame.Rect(1050, 200, 100, 100)
rect5 = pygame.Rect(412, 650, 100, 100)
rect6 = pygame.Rect(838, 650, 100, 100)
pygame.draw.rect(screen0,(153, 32, 28), rect2)
pygame.draw.rect(screen0,(153, 32, 28), rect3)
pygame.draw.rect(screen0,(153, 32, 28), rect4)
pygame.draw.rect(screen0,(153, 32, 28), rect5)
pygame.draw.rect(screen0, (153, 32, 28), rect6)
instruction = text2.render("SELECT THE AMOUNT OF PLAYERS IN YOU GAME!!!", True, (255, 255, 255))
screen0.blit(instruction, (50, 100))
twoplayer = text1.render("2", True, (255, 255, 255))
screen0.blit(twoplayer, (240, 225))
threeplayer = text1.render("3", True, (255, 255, 255))
screen0.blit(threeplayer, (660, 225))
fourplayer = text1.render("4", True, (255, 255, 255))
screen0.blit(fourplayer, (1085, 225))
fiveplayer = text1.render("5", True, (255, 255, 255))
screen0.blit(fiveplayer, (447, 675))
sixplayer = text1.render("6", True, ((255, 255, 255)))
screen0.blit(sixplayer, (873, 675))

numplayers = 0

