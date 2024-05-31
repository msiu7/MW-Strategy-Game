#CS Club Game

import pygame
import random
from array import *
from classes import *
from functions import *

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
screen0 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen0.fill(Background_color)
rect2 = pygame.Rect(200, 200, 100, 100)
rect3 = pygame.Rect(625, 200, 100, 100)
rect4 = pygame.Rect(1050, 200, 100, 100)
rect5 = pygame.Rect(412, 650, 100, 100)
rect6 = pygame.Rect(838, 650, 100, 100)
pygame.draw.rect(screen0,(153, 32, 28),rect2)
pygame.draw.rect(screen0,(153, 32, 28),rect3)
pygame.draw.rect(screen0,(153, 32, 28),rect4)
pygame.draw.rect(screen0,(153, 32, 28),rect5)
pygame.draw.rect(screen0, (153, 32, 28), rect6)

pygame.display.flip()
numplayers = 0
running0 = True 
while running0:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if rect2.collidepoint(event.pos):
                numplayers = 2
            
                #pygame.screen0.quit()
                running0 = False
            if rect3.collidepoint(event.pos):
                numplayers = 3
                
                running0 = False
            if rect4.collidepoint(event.pos):
                numplayers = 4
                
                running0 = False
            if rect5.collidepoint(event.pos):
                numplayers = 5
                
                running0 = False
            if rect6.collidepoint(event.pos):
                numplayers = 6
                
                running0 = False
    pygame.display.update()

for a in range(numplayers):
    players.append(player(str(a+1), "placeholdercolor"))
currentplayer = players[currentplayerindex] 


#Setting up Game Screen & Tiles
Background_color = (50, 168, 82)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 850
screen1 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen1.fill(Background_color)
grid = []
for row in range(30):
    temp_row = []
    for col in range(50):
        x = col * 25
        y = row * 25
        temp_row.append(oceanTile(x, y, 25, 25))
    grid.append(temp_row)

#Generate Map
genLand(random.randrange(0, 50), random.randrange(0, 30), grid)
while not isValidGen(grid): 
    genLand(10, 5, grid)
    if checkTotalLand(grid) > 700:
        break
    genLand(10, 25, grid)
    if checkTotalLand(grid) > 700:
        break    
    genLand(45, 5, grid)
    if checkTotalLand(grid) > 700:
        break
    genLand(45, 25, grid)
    if checkTotalLand(grid) > 700:
        break
    print(checkTotalLand(grid))
x = 0
count = 0
for col in range(50):
    grid[0][count] = oceanTile(x, 0, 25, 25)
    x += 25
    count += 1
x = 0
count = 0
for col in range(50):
    grid[29][count] = oceanTile(x, 725, 25, 25)
    x += 25
    count += 1
y = 0
count = 0
for row in range(30):
    grid[count][0] = oceanTile(0, y, 25, 25)
    count += 1
    y += 25
y = 0
count = 0
for row in range(30):
    grid[count][49] = oceanTile(1225, y, 25, 25)
    count += 1
    y += 25
removeIsolatedOcean(grid)
print(checkTotalLand(grid))
fixTextures(grid)
for a in range(70):
    CreateForest(grid)
for a in range(5):
    CreateMountains(grid)
randomizeTextures(grid)

#Giving all Land Tiles an ID
counter = 0
for row in range(30):
    for col in range(50):
            counter += 1
            grid[row][col].setID(counter)

#Creating Buttons

    #Background for UI Bar
backgroundUI = pygame.Rect(0, 750, 1250, 100)

    #End Turn Button
endturn = pygame.Rect(1150, 750, 100, 100)

    #Expansion View
expansionmode = pygame.Rect(1050, 750, 100, 100)

    #Ask If User Wants to Expand Button

yesExpand = pygame.Rect(525, 800, 50, 50)
noExpand = pygame.Rect(725, 800, 50, 50)
#Game Loop
running1 = True
while running1:  
    #currentplayer = players[currentplayerindex]    
    #Hovering Mouse
    mouse_pos = pygame.mouse.get_pos()  
    my = mouse_pos[1] // 25 
    mx = mouse_pos[0] // 25
    if my < 30:
        tilex = grid[my][mx].getCordsx() 
        tiley = grid[my][mx].getCordsy()
    wowzer = pygame.image.load('white.png')
    
    #Recreating Screen
    screen1.fill(Background_color)
    drawUI(screen1, backgroundUI, endturn)
    pygame.draw.rect(screen1, (21, 173, 41), yesExpand)
    pygame.draw.rect(screen1,(2, 24, 97),noExpand)
    
    #All User inputs work through this 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running1 = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            #Expansion
            if event.pos[1]//25 < 30:
                print("whywhwyhwhwhw")
                x = event.pos[0]//25
                y = event.pos[1]//25
            
                if yesExpand.collidepoint(event.pos):
                    currentplayer.addTerritoryToPlayer(grid[x][y].getID())
                    if currentplayerindex == 0:
                        grid[x][y].setTexture(pygame.image.load('red.png'))
                    if currentplayerindex == 1:
                        grid[x][y].setTexture(pygame.image.load('blue.jpg'))
                if noExpand.collidepoint(event.pos):
                    screen1.fill(Background_color)
               
            #Player Turn Cycling
            

            if endturn.collidepoint(event.pos):
                currentplayerindex += 1
                if currentplayerindex == numplayers:
                    currentplayerindex = 0
                    turnnumber += 1
                currentplayer = players[currentplayerindex]             

    text = pygame.font.SysFont("Arial", 30)
    textdraw = text.render(f"Player:{currentplayer.name}", True, (0, 0, 0))
    textturnnumber = text.render(f"Turn #{turnnumber}", True, (0, 0, 0))
    screen1.blit(textdraw, (1, 800))
    screen1.blit(textturnnumber, (1, 825))

    for row in range(30):
        for col in range(50):
            grid[row][col].draw(screen1)
            if tiley < 749:
                screen1.blit(wowzer, (tilex, tiley))
    
    pygame.display.update()