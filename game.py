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

    #Move Population Mode Button
movePopButtonMode = pygame.Rect(750, 750, 100, 100)
moveMode = pygame.Rect(775, 800, 50, 25)

    #Tile Level View Button
tileLevelView = pygame.Rect(650, 750, 100, 100)


    #Ask If User Wants to Expand Button
    #ultimate super dooper awesome loop!!!!!!!!!!
gaming = True
while gaming:

#Game Loop
    running1 = True
    battleview = False
    civview = False
    resourcedisplay1 = False
    movePopMode = False 
    levelView = False
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
        
        #Exit Button
        exitButton = pygame.Rect(975, 225, 50, 50)

        #Tile Improvement Button
        upgradeTileButton = pygame.Rect(600, 230, 200, 50)
        
        #Resource option
        resourcetab = pygame.Rect(1050, 750, 100, 100)
        pygame.draw.rect(screen1, (12, 69, 153), resourcetab)

        #Military Option
        pygame.draw.rect(screen1, (139, 124, 124), militaryview)

        #Tile Level View Option
        pygame.draw.rect(screen1, (255, 0, 0), tileLevelView)
        
        #All User inputs work through this 
        waitingForSecond = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                running1 = False
                civview = False
            
            
            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if militaryview.collidepoint(event.pos):
                    battleview = True
                    running1 = False
                if populationview.collidepoint(event.pos):
                    civview = True
                    running1 = False
                if tileLevelView.collidepoint(event.pos):
                    levelView = True
                    running1 = False
                if event.pos[1] // 25 < 30:
                    
                    
                    x = event.pos[0] // 25
                    y = event.pos[1] // 25

                    
                    
                    
                    
                    
                    
                    
                    
                    unownedWaitingForSecond = True
                    for a in range(0, len(players)):
                        if players[a].doesTileBelongToPlayer(grid[y][x].getID()):
                            unownedWaitingForSecond = False
                            break
                    
                    cost = popupText.render(f"Cost: {grid[y][x].tileValue} Gold", True, (0, 0, 0))
                    goToManage = popupText.render(f"Manage Population", True, (0, 0, 0))
                    if isinstance(grid[y][x], landTile):
                        goToUpgrade = popupText.render(f"Upgrade Tile", True, (0, 0, 0))
                        currentLevel = bigText.render(f"Level: {grid[y][x].level}", True, (0, 0, 0))
                    production1 = popupText.render(f"{grid[y][x].returnProduction1()}", True, (0, 0, 0))
                    production2 = popupText.render(f"{grid[y][x].returnProduction2()}", True, (0, 0, 0))
                    civiliansTile = popupText.render(f"Civilians: {grid[y][x].getCivLength()}", True, (0, 0, 0))
                    soldiersTile = popupText.render(f"Soldiers: {grid[y][x].getSolLength()}", True, (0, 0, 0))
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
                                goToManageButton = pygame.Rect((x * 25) + 50, (y * 25) + 125, 100, 25)
                                if isinstance(grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) + 50, (y * 25) + 95, 100, 25)
                                productionXposition = x * 25 + 55
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 51
                                civiliansTileYPosition = y * 25 + 63
                                soldiersTileYPosition = y * 25 + 75
                                goToManageYPosition = y * 25 + 130
                                goToUpgradeYPosition = y * 25 + 100
                            else:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) - 150, 150, 150)
                                exitButton = pygame.Rect((x * 25) + 25, (y * 25) - 25, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) + 50, (y * 25) - 50, 100, 25)
                                if isinstance(grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) + 50, (y * 25) - 80, 100, 25)
                                productionXposition = x * 25 + 55
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 45
                                goToUpgradeYPosition = y * 25 - 75
                       else:
                            if grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) - 150, (y * 25) + 25, 150, 150)
                                exitButton = pygame.Rect((x * 25) - 150, (y * 25) + 150, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) - 128, (y * 25) + 125, 100, 25)
                                if isinstance(grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) - 128, (y * 25) + 95, 100, 25)
                                productionXposition = x * 25 - 123
                                production1YPosition = y * 25 + 37
                                production2YPosition = y * 25 + 49
                                civiliansTileYPosition = y * 25 + 61
                                soldiersTileYPosition = y * 25 + 73
                                goToManageYPosition = y * 25 + 130
                                goToUpgradeYPosition = y * 25 + 100
                            else:
                                popuprect = pygame.Rect((x * 25) - 150, (y * 25) - 150, 150, 150)
                                exitButton = pygame.Rect((x * 25) - 150, (y * 25) - 25, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) - 128, (y * 25) - 50, 100, 25)
                                if isinstance(grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) - 128, (y * 25) - 80, 100, 25)
                                productionXposition = x * 25 - 123
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 45
                                goToUpgradeYPosition = y * 25 - 75

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
                        if isinstance(grid[y][x], landTile):
                            pygame.draw.rect(screen1, (255, 255, 255), goToUpgradeButton)
                            screen1.blit(goToUpgrade, (productionXposition, goToUpgradeYPosition))
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
      
                                #This function is for Land Tiles only
                                if goToUpgradeButton.collidepoint(event.pos) and isinstance(grid[y][x], landTile):
                                    isUpgradingTile = True
                                    exitButton = pygame.Rect(975, 225, 50, 50)
                                    upgradeTileButton = pygame.Rect(600, 300, 200, 50)
                                    
                                    clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 50 Brick", True, (0, 0, 0))
                                    if grid[y][x].level == 1:
                                        clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 50 Brick", True, (0, 0, 0))
                                    elif grid[y][x].level == 2:
                                        clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 100 Brick", True, (0, 0, 0))
                                    elif grid[y][x].level == 3:
                                        clickToUpgradeTile = bigText.render(f"Tile Maxed Out", True, (0, 0, 0))
                                    
                                    while isUpgradingTile:
                                        for row in range(30):
                                            for col in range(50):
                                                grid[row][col].draw(screen1)                                        
                                        
                                        pygame.draw.rect(screen1, (211, 182, 131), managescreen)
                                        pygame.draw.rect(screen1, (255, 0, 0), exitButton)
                                        pygame.draw.rect(screen1, (255, 255, 255), upgradeTileButton)
                                        screen1.blit(currentLevel, (250, 350))
                                        screen1.blit(clickToUpgradeTile, (250, 400))
                                        pygame.display.update()
 
                                        for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                if exitButton.collidepoint(event.pos):
                                                    isUpgradingTile = False
                                                    tilePopup = False
                                                    break
                                                if upgradeTileButton.collidepoint(event.pos):
                                                    if grid[y][x].level == 1:
                                                        if currentplayer.getBrick() >= 50:
                                                            grid[y][x].upgradeTile(currentplayer)
                                                            clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 100 Brick", True, (0, 0, 0))
                                                            pygame.display.update()
                                                    elif grid[y][x].level == 2:
                                                        if currentplayer.getBrick() >= 100:
                                                            grid[y][x].upgradeTile(currentplayer)
                                                            clickToUpgradeTile = bigText.render(f"Tile Maxed Out", True, (0, 0, 0))
                                                            pygame.display.update()
                                                    else:
                                                        break
                                                    currentLevel = bigText.render(f"Level: {grid[y][x].level}", True, (0, 0, 0))
                                                    screen1.blit(currentLevel, (250, 350))
                                                    
                                                    pygame.display.update()
                                                        
                                
                                if goToManageButton.collidepoint(event.pos):
                                                  
                                    isManagingPopulation = True
                                    while isManagingPopulation:
                                        for row in range(30):
                                            for col in range(50):
                                                grid[row][col].draw(screen1)
                                        unemployedTile = bigText.render(f"Unemployed: {grid[y][x].getUnemployedLength()}", True, (0, 0, 0))
                                        civiliansTile = bigText.render(f"Civilians: {grid[y][x].getCivLength()}", True, (0, 0, 0))
                                        soldiersTile = bigText.render(f"Soldiers: {grid[y][x].getSolLength()}", True, (0, 0, 0))
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
                                                    if grid[y][x].getUnemployedLength() > 0:
                                                        grid[y][x].population[grid[y][x].findIndexOfType("unemployed")].changeType("civilian")
                                                        print(f"Civ: {grid[y][x].getCivLength()}")
                                                        print(f"Sol:{grid[y][x].getSolLength()}")
                                                        print(f"Un:{grid[y][x].getUnemployedLength()}")
                                                if poptosol.collidepoint(event.pos):
                                                    if grid[y][x].getUnemployedLength() > 0:
                                                        grid[y][x].population[grid[y][x].findIndexOfType("unemployed")].changeType("soldier")
                                                        print(f"Civ: {grid[y][x].getCivLength()}")
                                                        print(f"Sol:{grid[y][x].getSolLength()}")
                                                        print(f"Un:{grid[y][x].getUnemployedLength()}")           
                                                if soltociv.collidepoint(event.pos):
                                                    if grid[y][x].getSolLength() > 0:  
                                                        grid[y][x].population[grid[y][x].findIndexOfType("soldier")].changeType("civilian")
                                                        print(f"Civ: {grid[y][x].getCivLength()}")
                                                        print(f"Sol:{grid[y][x].getSolLength()}")
                                                        print(f"Un:{grid[y][x].getUnemployedLength()}")
                                                if civtosol.collidepoint(event.pos):
                                                    if grid[y][x].getCivLength() > 0:
                                                        grid[y][x].population[grid[y][x].findIndexOfType("civilian")].changeType("soldier")
                                                        print(f"Civ: {grid[y][x].getCivLength()}")
                                                        print(f"Sol:{grid[y][x].getSolLength()}")
                                                        print(f"Un:{grid[y][x].getUnemployedLength()}")                              

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
                                    if currentplayer.getGold() >= grid[y][x].tileValue:
                                        if currentplayer.checkExpandable(grid[y][x].getID(), grid):
                                            if not(len(currentplayer.territories) == 0 and isinstance(grid[y][x], oceanTile)):
                                                currentplayer.subtractGold(grid[y][x].tileValue)                           
                                                currentplayer.addTerritoryToPlayer(grid[y][x].getID())
                                                if isinstance(grid[y][x],landTile):
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
                currentplayer.updateFunctionalProductionValues(grid)
                currentplayer.updateProductionValues(grid)
                foodPerTurn = text.render(f"{currentplayer.foodperturn - currentplayer.foodConsumption}", True, (0, 0, 0))
                screen1.blit(foodPerTurn, (675, 60))
                stonePerTurn = text.render(f"{currentplayer.stoneperturn}", True, (0, 0, 0))
                screen1.blit(stonePerTurn, (775, 60))
                woodPerTurn = text.render(f"{currentplayer.woodperturn}", True, (0, 0, 0))
                screen1.blit(woodPerTurn, (875, 60))
                
        pygame.display.update()
    
    screen2 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while civview:
        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen2)
        for a in range(0, len(players)):
            players[a].drawBorders(screen2)
            players[a].addBordering()
            if not a == currentplayerindex:
                for b in range(0, len(players[a].territories)):
                    for c in range(0, len(currentplayer.territories)):
                        if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True:
                            temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                            pygame.draw.rect(screen2, (211, 182, 131), temprect)
                            popnumbers = text3.render(f"{grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].getCivLength()}", True, (255, 255, 255))
                            screen2.blit(popnumbers, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
        for a in range(0, len(currentplayer.territories)):
            temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
            pygame.draw.rect(screen2, (211, 182, 131), temprect)
            popnumbers = text3.render(f"{grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getCivLength()}", True, (255, 255, 255))
            screen2.blit(popnumbers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen2)
        pygame.draw.rect(screen2, (29, 158, 29), populationview)
        pygame.draw.rect(screen2, (114, 9, 219), movePopButtonMode)
        popOnOrOff = text.render(("Move:"), True, (255, 255, 255))
        if movePopMode == False:
            print(0)
            pygame.draw.rect(screen2, (255, 0, 0), moveMode)
        else:
            print(1)
            pygame.draw.rect(screen2, (0, 255, 0), moveMode)
        screen2.blit(popOnOrOff, (760, 760))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if populationview.collidepoint(event.pos):
                    civview = False
                    running1 = True
                if movePopButtonMode.collidepoint(event.pos):
                    if movePopMode == True:
                        movePopMode = False
                        pygame.draw.rect(screen2, (255, 0, 0), moveMode)
                    else:
                        movePopMode = True
                        pygame.draw.rect(screen2, (0, 255, 0), moveMode)
                    pygame.display.flip()
        while movePopMode == True:
            
            waitingforclick = True
            while waitingforclick:
                for a in range(0, len(currentplayer.territories)):
                    temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                    pygame.draw.rect(screen2, (211, 182, 131), temprect)
                    popcivilians = text3.render(f"{grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getCivLength()}", True, (255, 255, 255))
                    screen2.blit(popcivilians, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[1] // 25 < 30:
                            tilecol1 = event.pos[0] // 25
                            tilerow1 = event.pos[1] // 25
                            print("click1")
                            waitingforclick2 = True
                            while waitingforclick2: 
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.pos[1] // 25 < 30:
                                            tilecol2 = event.pos[0] // 25
                                            tilerow2 = event.pos[1] // 25
                                            print("click2")
                                            #LandTiles always need to have at least 1 population, OceanTiles don't
                                            if isinstance(grid[tilerow1][tilecol1], landTile):
                                                if ((len(grid[tilerow1][tilecol1].population)) > 1 and currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID())):
                                                    grid[tilerow1][tilecol1].population[grid[tilerow1][tilecol1].findIndexOfType("civilian")].movePopulation(grid[tilerow1][tilecol1].findIndexOfType("civilian"), tilerow1, tilecol1, tilerow2, tilecol2, grid)
                                            else:
                                                if ((len(grid[tilerow1][tilecol1].population)) > 0 and currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID())):
                                                    grid[tilerow1][tilecol1].population[grid[tilerow1][tilecol1].findIndexOfType("civilian")].movePopulation(grid[tilerow1][tilecol1].findIndexOfType("civilian"), tilerow1, tilecol1, tilerow2, tilecol2, grid)
                                            waitingforclick = False
                                            waitingforclick2 = False
                        elif movePopButtonMode.collidepoint(event.pos):
                            movePopMode = False
                            waitingforclick = False
                        
                

            
       
    screen3 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #  = pygame.Rect(1050, 750, 100, 100)              
    while battleview:
        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen3)
        for a in range(0, len(players)):
            players[a].drawBorders(screen3)
            players[a].addBordering()
            if not a == currentplayerindex:
                for b in range(0, len(players[a].territories)):
                    for c in range(0, len(currentplayer.territories)):
                        if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True:
                            temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                            pygame.draw.rect(screen3, (211, 182, 131), temprect)
                            popsoldiers = text3.render(f"{grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].getSolLength()}", True, (255, 255, 255))
                            screen3.blit(popsoldiers, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
        for a in range(0, len(currentplayer.territories)):
            temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
            pygame.draw.rect(screen3, (211, 182, 131), temprect)
            popsoldiers = text3.render(f"{grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getSolLength()}", True, (255, 255, 255))
            screen3.blit(popsoldiers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen3)
        pygame.draw.rect(screen3, (139, 124, 124), militaryview)
        pygame.draw.rect(screen3, (114, 9, 219), movePopButtonMode)
        popOnOrOff = text.render(("Move:"), True, (255, 255, 255))
        if movePopMode == False:
            print(0)
            pygame.draw.rect(screen3, (255, 0, 0), moveMode)
        else:
            print(1)
            pygame.draw.rect(screen3, (0, 255, 0), moveMode)
        screen3.blit(popOnOrOff, (760, 760))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if militaryview.collidepoint(event.pos):
                    battleview = False
                    running1 = True
                if movePopButtonMode.collidepoint(event.pos):
                    if movePopMode == True:
                        movePopMode = False
                        pygame.draw.rect(screen3, (255, 0, 0), moveMode)
                    else:
                        movePopMode = True
                        pygame.draw.rect(screen3, (0, 255, 0), moveMode)
                    pygame.display.flip()
        while movePopMode == True:
            
            waitingforclick = True
            while waitingforclick:
                for a in range(0, len(currentplayer.territories)):
                    temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                    pygame.draw.rect(screen3, (211, 182, 131), temprect)
                    popsoldiers = text3.render(f"{grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getSolLength()}", True, (255, 255, 255))
                    screen3.blit(popsoldiers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
                    pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.pos[1] // 25 < 30:
                            tilecol1 = event.pos[0] // 25
                            tilerow1 = event.pos[1] // 25
                            print("click1")
                            waitingforclick2 = True
                            while waitingforclick2: 
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if event.pos[1] // 25 < 30:
                                            tilecol2 = event.pos[0] // 25
                                            tilerow2 = event.pos[1] // 25
                                            print("click2")
                                            #LandTiles always need to have at least 1 population, OceanTiles don't
                                            if isinstance(grid[tilerow1][tilecol1], landTile):
                                                if ((len(grid[tilerow1][tilecol1].population)) > 1 and currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID())):
                                                    grid[tilerow1][tilecol1].population[grid[tilerow1][tilecol1].findIndexOfType("soldier")].movePopulation(grid[tilerow1][tilecol1].findIndexOfType("soldier"), tilerow1, tilecol1, tilerow2, tilecol2, grid)
                                                if (not(currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID()))) and checkPureAdjacency(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID()):
                                                    print("got through")
                                                    #check if both tiles are owned, if both are land, and if the attacking player has enough population to invade
                                                    if istileowned(tilecol2, tilerow2, players, grid, numplayers) and isinstance(grid[tilerow2][tilecol2], landTile) and (len(grid[tilerow1][tilecol1].population)) > 1:    
                                                        print("LAND BATTLE TIME")
                                                        #the actual battle square here
                                                        landBattle(currentplayer, players[findPlayerFromTile(grid[tilerow2][tilecol2].getID(), players)], grid)
                                            else:
                                                if ((len(grid[tilerow1][tilecol1].population)) > 0 and currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID())):
                                                    grid[tilerow1][tilecol1].population[grid[tilerow1][tilecol1].findIndexOfType("soldier")].movePopulation(grid[tilerow1][tilecol1].findIndexOfType("soldier"), tilerow1, tilecol1, tilerow2, tilecol2, grid)
                                                if (not(currentplayer.checkAdjacencyForMovement(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID()))) and checkPureAdjacency(grid[tilerow1][tilecol1].getID(), grid[tilerow2][tilecol2].getID()):
                                                    print("got through")
                                                    if istileowned(tilecol2, tilerow2, players, grid, numplayers):
                                                        if isinstance(grid[tilerow2][tilecol2], landTile):    
                                                            print("AMPHIBIOUS ATTACK")
                                                        else:
                                                            print("NAVAL BATTLE")   
                                            waitingforclick = False
                                            waitingforclick2 = False
                        elif movePopButtonMode.collidepoint(event.pos):
                            movePopMode = False
                            waitingforclick = False

    screen4 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while levelView:                        
        for row in range(30):
            for col in range(50):
                grid[row][col].draw(screen4)
        for a in range(0, len(players)):
            players[a].drawBorders(screen4)
            players[a].addBordering()
            if not a == currentplayerindex:
                print("1")
                for b in range(0, len(players[a].territories)):
                    print("2")
                    for c in range(0, len(currentplayer.territories)):
                        print("3")
                        #only make rectangles for land tiles (for opponents)
                        if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True and isinstance(grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50], landTile):
                            print("4")
                            temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                            pygame.draw.rect(screen4, (211, 182, 131), temprect)
                            level = text3.render(f"{grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].level}", True, (255, 255, 255))
                            screen4.blit(level, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
        for a in range(0, len(currentplayer.territories)):
            #only make rectangles for land tiles (for currentplayer)
            if isinstance(grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50], landTile):
                temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                pygame.draw.rect(screen4, (211, 182, 131), temprect)
                level = text3.render(f"{grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].level}", True, (255, 255, 255))
                screen4.blit(level, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen4)
        pygame.draw.rect(screen1, (255, 0, 0), tileLevelView)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tileLevelView.collidepoint(event.pos):
                    levelView = False
                    running1 = True
        pygame.display.flip()
