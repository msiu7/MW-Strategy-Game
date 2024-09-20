#CS Club Game

import pygame
import random
from array import *
from classes import *
from functions import *

#Things To Work On

#UI Buttons
#Give Each Tile Resources depending on type
#Give each player starting resources
#Give each tile a cost
#Population should increase every turn depending on food and capacity
#Army is created by taking population from a tile
#Create textures for settlement, village, city, mine, farmland?




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
pygame.draw.rect(screen0,(153, 32, 28),rect2)
pygame.draw.rect(screen0,(153, 32, 28),rect3)
pygame.draw.rect(screen0,(153, 32, 28),rect4)
pygame.draw.rect(screen0,(153, 32, 28),rect5)
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
    players.append(player(str(a+1), str(a+1)))
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
fixCoastalTextures(grid)
for a in range(75):
    CreateForest(grid)
while checkTotalMountain(grid) < 60:
    CreateMountains(grid)
createPlainsTiles(grid)
randomizeTextures(grid)
fixMountainTextures(grid)
#Giving all Land Tiles an ID
counter = -1
for row in range(30):
    for col in range(50):
            counter += 1
            grid[row][col].setID(counter)
giveTilesProduction(grid)
#Creating Buttons

    #Background for UI Bar
backgroundUI = pygame.Rect(0, 750, 1250, 100)

    #End Turn Button
endturn = pygame.Rect(1150, 750, 100, 100)

    #Expansion View
expansionmode = pygame.Rect(1050, 750, 100, 100)

    #Population View
populationview = pygame.Rect(950, 750, 100, 100)

    #Military View
militaryview = pygame.Rect(850, 750, 100, 100)


    #Ask If User Wants to Expand Button
    #ultimate super dooper awesome loop!!!!!!!!!!
gaming = True
while gaming:

#Game Loop
    running1 = True
    battleview = False
    popview = False
    resourcedisplay1 = False 
    while running1:
        
        popupText = pygame.font.SysFont("Arial", 10)
        bigText = pygame.font.SysFont("Arial", 30)
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
        pygame.draw.rect(screen1, (29, 158, 29), populationview)
        
        #Resource option
        resourcetab = pygame.Rect(1050, 750, 100, 100)
        pygame.draw.rect(screen1, (12, 69, 153), resourcetab)

        #Military Option
        pygame.draw.rect(screen1, (139, 124, 124), militaryview)
        
        #All User inputs work through this 
        waitingForSecond = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                running1 = False
                popview = False
            
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if militaryview.collidepoint(event.pos):
                    battleview = True
                    running1 = False
                if populationview.collidepoint(event.pos):
                    popview = True
                    running1 = False
                if event.pos[1] // 25 < 30:
                    
                    
                    x = event.pos[0] // 25
                    y = event.pos[1] // 25

                    
                    
                    
                    
                    
                    
                    
                    
                    unownedWaitingForSecond = True
                    for a in range(0, len(players)):
                        if players[a].doesTileBelongToPlayer(grid[y][x].getID()):
                            unownedWaitingForSecond = False
                            break
                    
                    cost = popupText.render(f"Cost: {grid[y][x].returnValue()} Gold", True, (0, 0, 0))
                    goToManage = popupText.render(f"Manage Population", True, (0, 0, 0))
                    production1 = popupText.render(f"{grid[y][x].returnProduction1()}", True, (0, 0, 0))
                    production2 = popupText.render(f"{grid[y][x].returnProduction2()}", True, (0, 0, 0))
                    civiliansTile = popupText.render(f"Civilians: {len(grid[y][x].civilians)}", True, (0, 0, 0))
                    soldiersTile = popupText.render(f"Soldiers: {len(grid[y][x].soldiers)}", True, (0, 0, 0))
                    production1YPosition = 0
                    production2YPosition = 0
                    productionXposition = 0
                    costXPosition = 0
                    costYPosition = 0
                    goToManageYPosition = 0

                    tilePopup = False
                    if currentplayer.doesTileBelongToPlayer(grid[y][x].getID()):
                       tilePopup = True                 
                       if grid[y][x].getCol() < 25:
                            if grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) + 25, 150, 150)
                                exitButton = pygame.Rect((x * 25) + 25, (y * 25) + 150, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) + 50, (y * 25) + 115, 100, 25)
                                productionXposition = x * 25 + 55
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 51
                                civiliansTileYPosition = y * 25 + 63
                                soldiersTileYPosition = y * 25 + 75
                                goToManageYPosition = y * 25 + 120
                            else:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) - 150, 150, 150)
                                exitButton = pygame.Rect((x * 25) + 25, (y * 25) - 25, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) + 50, (y * 25) - 60, 100, 25)
                                productionXposition = x * 25 + 55
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 55
                       else:
                            if grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) - 150, (y * 25) + 25, 150, 150)
                                exitButton = pygame.Rect((x * 25) - 150, (y * 25) + 150, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) - 128, (y * 25) + 115, 100, 25)
                                productionXposition = x * 25 - 123
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 49
                                civiliansTileYPosition = y * 25 + 61
                                soldiersTileYPosition = y * 25 + 73
                                goToManageYPosition = y * 25 + 120
                            else:
                                popuprect = pygame.Rect((x * 25) - 150, (y * 25) - 150, 150, 150)
                                exitButton = pygame.Rect((x * 25) - 150, (y * 25) - 25, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) - 128, (y * 25) - 60, 100, 25)
                                productionXposition = x * 25 - 123
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 55

                    else:
                        if grid[y][x].getCol() < 25:
                            if grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) + 25, 100, 100)
                                yesExpand = pygame.Rect((x * 25) + 25, (y * 25) + 115, 50, 10)
                                noExpand = pygame.Rect((x * 25) + 75, (y * 25) + 115, 50, 10)
                                costXPosition = x * 25 + 27
                                costYPosition = y * 25 + 25
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 49
                            else:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) - 125, 100, 100)
                                yesExpand = pygame.Rect((x * 25) + 25, (y * 25) - 35, 50, 10)
                                noExpand = pygame.Rect((x * 25) + 75, (y * 25) - 35, 50, 10)
                                costXPosition = x * 25 + 27
                                costYPosition = y * 25 - 125
                                production1YPosition = y * 25 - 113
                                production2YPosition = y * 25 - 101
                        else:
                            if grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) - 125, (y * 25) + 25, 100, 100)
                                yesExpand = pygame.Rect((x * 25) - 125, (y * 25) + 115, 50, 10)
                                noExpand = pygame.Rect((x * 25) - 75, (y * 25) + 115, 50, 10)
                                costXPosition = x * 25 - 123
                                costYPosition = y * 25 + 25
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 49
                            else:
                                popuprect = pygame.Rect((x * 25) - 125, (y * 25) - 125, 100, 100)
                                yesExpand = pygame.Rect((x * 25) - 125, (y * 25) - 35, 50, 10)
                                noExpand = pygame.Rect((x * 25) - 75, (y * 25) - 35, 50, 10)
                                costXPosition = x * 25 - 123
                                costYPosition = y * 25 - 125
                                production1YPosition = y * 25 - 113
                                production2YPosition = y * 25 - 101
                        
                    

                    while tilePopup:

                        for row in range(30):
                            for col in range(50):
                                grid[row][col].draw(screen1)

                        pygame.draw.rect(screen1, (211, 182, 131), popuprect)
                        pygame.draw.rect(screen1, (209, 27, 27), exitButton)
                        pygame.draw.rect(screen1, (255, 255, 255), goToManageButton)
                        managescreen = pygame.Rect(225, 225, 800, 300)
                        screen1.blit(production1, (productionXposition, production1YPosition))
                        screen1.blit(production2, (productionXposition, production2YPosition))
                        screen1.blit(civiliansTile, (productionXposition, civiliansTileYPosition))
                        screen1.blit(soldiersTile, (productionXposition, soldiersTileYPosition))
                        screen1.blit(goToManage, (productionXposition, goToManageYPosition))
                        screen1.blit(wowzer, (x*25, y*25))
                        
                        pygame.display.update()

                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if exitButton.collidepoint(event.pos):
                                    screen1.fill(Background_color)
                                    tilePopup = False
                                    break
                                if goToManageButton.collidepoint(event.pos):
                                                  
                                    isManagingPopulation = True
                                    while isManagingPopulation:
                                        for row in range(30):
                                            for col in range(50):
                                                grid[row][col].draw(screen1)
                                        unemployedTile = bigText.render(f"Unemployed: {len(grid[y][x].population) - len(grid[y][x].civilians)-len(grid[y][x].soldiers)}", True, (0, 0, 0))
                                        civiliansTile = bigText.render(f"Civilians: {len(grid[y][x].civilians)}", True, (0, 0, 0))
                                        soldiersTile = bigText.render(f"Soldiers: {len(grid[y][x].soldiers)}", True, (0, 0, 0))
                                        exitButton = pygame.Rect(975, 225, 50, 50)
                                        pygame.draw.rect(screen1, (211, 182, 131), managescreen)
                                        screen1.blit(civiliansTile, (235, 230))
                                        screen1.blit(soldiersTile, (235, 355))
                                        screen1.blit(unemployedTile, (235, 470))
                                        poptociv = pygame.Rect(495, 465, 200, 50)
                                        poptosol = pygame.Rect(715, 465, 200, 50)
                                        soltociv = pygame.Rect(600, 355, 200, 50)
                                        civtosol = pygame.Rect(600, 230, 200, 50)
                                        pygame.draw.rect(screen1, (255, 0, 0), exitButton)
                                        pygame.draw.rect(screen1, (255, 255, 255), poptociv)
                                        pygame.draw.rect(screen1, (255, 255, 255), poptosol)
                                        pygame.draw.rect(screen1, (255, 255, 255), soltociv)
                                        pygame.draw.rect(screen1, (255, 255, 255), civtosol)
                                        pygame.display.update()
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if exitButton.collidepoint(event.pos):
                                                    isManagingPopulation = False
                                                    tilePopup = False
                                                    break
                                                if poptociv.collidepoint(event.pos):
                                                    if len(grid[y][x].population) - len(grid[y][x].civilians) - len(grid[y][x].soldiers)  > 0:
                                                        grid[y][x].popToCivilian(0, y, x)
                                                if poptosol.collidepoint(event.pos):
                                                    if len(grid[y][x].population) - len(grid[y][x].civilians) - len(grid[y][x].soldiers)  > 0:
                                                        grid[y][x].popToSoldier(0, y, x)
                                                if soltociv.collidepoint(event.pos):
                                                    if len(grid[y][x].soldiers) > 0:  
                                                        grid[y][x].solToCivilian(0, y, x)  
                                                if civtosol.collidepoint(event.pos):
                                                    if len(grid[y][x].civilians) > 0:
                                                        grid[y][x].civToSoldier(0, y, x)
                    
                    
                    while unownedWaitingForSecond:
                        
                        for row in range(30):
                            for col in range(50):
                                grid[row][col].draw(screen1)
                        

                        
                        pygame.draw.rect(screen1, (211, 182, 131), popuprect)
                        pygame.draw.rect(screen1, (34, 227, 50), yesExpand)
                        pygame.draw.rect(screen1, (209, 27, 27), noExpand)
                        screen1.blit(cost, (costXPosition, costYPosition))
                        screen1.blit(production1, (costXPosition, production1YPosition))
                        screen1.blit(production2, (costXPosition, production2YPosition))
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if yesExpand.collidepoint(event.pos):
                                    if currentplayer.getGold() >= grid[y][x].returnValue():
                                        if currentplayer.checkExpandable(grid[y][x].getID(), grid):
                                            currentplayer.subtractGold(grid[y][x].returnValue())                           
                                            currentplayer.addTerritoryToPlayer(grid[y][x].getID())
                                            grid[y][x].manuallyAddPopulation(1)
                                            currentplayer.totalPlayerPopulation(grid)
                                            currentplayer.updateFunctionalProductionValues(grid)
                                            currentplayer.updateProductionValues(grid)
                                            
                                            
                                if noExpand.collidepoint(event.pos):
                                    screen1.fill(Background_color)
                                unownedWaitingForSecond = False
                    
                    
                if resourcedisplay1: 
                    if resourcetab.collidepoint(event.pos):
                        resourcedisplay1 = False
                        
                elif not resourcedisplay1:         
                    if resourcetab.collidepoint(event.pos):
                        resourcedisplay1 = True
                #Player Turn Cycling
                if endturn.collidepoint(event.pos):
                    currentplayerindex += 1
                    currentplayer.endTurnSequence(grid)
                    if currentplayerindex == numplayers:
                        currentplayerindex = 0
                        turnnumber += 1
                    currentplayer = players[currentplayerindex]
                    resourcedisplay1 = False
                    


                            
        #player count display
        
        textdraw = text.render(f"Player: {currentplayer.name}", True, (0, 0, 0))
        textturnnumber = text.render(f"Turn #{turnnumber}", True, (0, 0, 0))
        screen1.blit(textdraw, (10, 760))
        screen1.blit(textturnnumber, (10, 810))

        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen1)
                if tiley < 749:
                    screen1.blit(wowzer, (tilex, tiley))
        
        
        for a in range(0, len(players)):
            players[a].drawBorders(screen1)
            players[a].addBordering()
        
        #Resource display
        if resourcedisplay1:
                #popupText = pygame.font.SysFont("Arial", 10)
                resourcedisplay = pygame.Rect(200, 25, 850, 100)
                pygame.draw.rect(screen1, (211, 182, 131), resourcedisplay)
                #Icons/Labels
                perTurnLabel = text.render(f"Per Turn:", True, (0, 0, 0))
                screen1.blit(perTurnLabel, (300, 60))
                totalLabel = text.render(f"Total:", True, (0, 0, 0))
                screen1.blit(totalLabel, (300, 90))
                resourcesLabel = text.render(f"Resources:", True, (0, 0, 0))
                screen1.blit(resourcesLabel, (300, 30))
                goldIcon = text.render(f"Gold", True, (0, 0, 0))
                screen1.blit(goldIcon, (475, 30))
                brickIcon = text.render(f"Brick", True, (0, 0, 0))
                screen1.blit(brickIcon, (575, 30))
                foodIcon = text.render(f"Food", True, (0, 0, 0))
                screen1.blit(foodIcon, (675, 30))
                stoneIcon = text.render(f"Stone", True, (0, 0, 0))
                screen1.blit(stoneIcon, (775, 30))
                woodIcon = text.render(f"Wood", True, (0, 0, 0))
                screen1.blit(woodIcon, (875, 30))
                
                totalGold = text.render(f"{currentplayer.getGold()}", True, (0, 0, 0))
                screen1.blit(totalGold, (475, 90))
                totalBrick = text.render(f"{currentplayer.getBrick()}", True, (0, 0, 0))
                screen1.blit(totalBrick, (575, 90))
                totalFood = text.render(f"{currentplayer.getFood()}", True, (0, 0, 0))
                screen1.blit(totalFood, (675, 90))
                totalStone = text.render(f"{currentplayer.getStone()}", True, (0, 0, 0))
                screen1.blit(totalStone, (775, 90))
                totalWood = text.render(f"{currentplayer.getWood()}", True, (0, 0, 0))
                screen1.blit(totalWood, (875, 90))
                
                goldPerTurn = text.render(f"{currentplayer.goldperturn}", True, (0, 0, 0))
                screen1.blit(goldPerTurn, (475, 60))
                brickPerTurn = text.render(f"{currentplayer.brickperturn}", True, (0, 0, 0))
                screen1.blit(brickPerTurn, (575, 60))
                currentplayer.updateFoodConsumption()
                foodPerTurn = text.render(f"{currentplayer.foodperturn - currentplayer.foodConsumption}", True, (0, 0, 0))
                screen1.blit(foodPerTurn, (675, 60))
                stonePerTurn = text.render(f"{currentplayer.stoneperturn}", True, (0, 0, 0))
                screen1.blit(stonePerTurn, (775, 60))
                woodPerTurn = text.render(f"{currentplayer.woodperturn}", True, (0, 0, 0))
                screen1.blit(woodPerTurn, (875, 60))
                
        pygame.display.update()
    
    screen2 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while popview:
        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen2)
        for a in range(0, len(currentplayer.territories)):
            temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
            pygame.draw.rect(screen2, (211, 182, 131), temprect)
            popnumbers = text3.render(f"{len(grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].population)}", True, (255, 255, 255))
            screen2.blit(popnumbers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen2)
        pygame.draw.rect(screen2, (29, 158, 29), populationview)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if populationview.collidepoint(event.pos):
                    popview = False
                    running1 = True
            
       
    screen3 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #  = pygame.Rect(1050, 750, 100, 100)              
    while battleview:
        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen3)
        for a in range(0, len(currentplayer.territories)):
            temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
            pygame.draw.rect(screen3, (211, 182, 131), temprect)
            popsoldiers = text3.render(f"{len(grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].soldiers)}", True, (255, 255, 255))
            screen3.blit(popsoldiers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen3)
        pygame.draw.rect(screen3, (29, 158, 29), militaryview)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if militaryview.collidepoint(event.pos):
                    battleview = False
                    running1 = True
        
        
