#CS Club Game

import pygame
from globals import *
from array import *
from basicResourceViewSetup import *
from player import *
from functions import *
from oceanTile import oceanTile
from gameMap import gameMap
from managePopulation import managePopulation
from move import *

pygame.display.flip()
running0 = True 
while running0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running0 = False
        if event.type == pygame.MOUSEBUTTONDOWN:       
            if rect2.collidepoint(event.pos):
                numplayers = 2
            elif rect3.collidepoint(event.pos):
                numplayers = 3
            elif rect4.collidepoint(event.pos):
                numplayers = 4
            elif rect5.collidepoint(event.pos):
                numplayers = 5
            elif rect6.collidepoint(event.pos):
                numplayers = 6
            if(numplayers != 0):
                for a in range(numplayers):
                    players.append(player(str(a+1), str(a+1)))
                currentplayer = players[currentplayerindex]        
                running0 = False
    pygame.display.update()

#Setting up Game Screen & Tiles
Background_color = (50, 168, 82)
SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 850
screen1 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
screen1.fill(Background_color)
mainMap = gameMap()
mainMap.buildMap()

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

    #Spelunking Results Button
spelunkingResultsView = pygame.Rect(550, 750, 100, 100)

    #Ask If User Wants to Expand Button
    #ultimate super dooper awesome loop!!!!!!!!!!
gaming = True
while gaming and numplayers != 0:

#Game Loop
    running1 = True
    battleview = False
    civview = False
    resourcedisplay1 = False
    resourcedisplay2 = False
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
            tilex = mainMap.grid[my][mx].getCordsx() 
            tiley = mainMap.grid[my][mx].getCordsy()
        wowzer = pygame.image.load('Graphics/white.png')
        
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

        #Spelunking Results Option
        pygame.draw.rect(screen1, (219, 3, 252), spelunkingResultsView)
        
        #All User inputs work through this 
        waitingForSecond = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gaming = False
                running1 = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                if militaryview.collidepoint(event.pos): #event 1
                    battleview = True
                    running1 = False

                if populationview.collidepoint(event.pos): #event 2
                    civview = True
                    running1 = False

                if tileLevelView.collidepoint(event.pos): #event 3
                    levelView = True
                    running1 = False
                
                if resourcetab.collidepoint(event.pos): #event 4
                    if resourcedisplay1:
                        resourcedisplay1 = False
                    else:
                        resourcedisplay1 = True
                    resourcedisplay2 = False

                if spelunkingResultsView.collidepoint(event.pos): #event 5
                    if resourcedisplay2:
                        resourcedisplay2 = False
                    else:
                        resourcedisplay2 = True
                    resourcedisplay1 = False 

                    #The lines at the end of events 4 & 5 allow for switching between the production view and treasure view

                
                #Player Turn Cycling
                if endturn.collidepoint(event.pos): #event 6
                    currentplayerindex += 1
                    currentplayer.endTurnSequence(mainMap)
                    if currentplayerindex == numplayers:
                        currentplayerindex = 0
                        turnnumber += 1
                    currentplayer = players[currentplayerindex]
                    resourcedisplay1 = False
                    resourcedisplay2 = False

                if event.pos[1] // 25 < 30:
                    
                    
                    x = event.pos[0] // 25
                    y = event.pos[1] // 25

                    
                    
                    
                    
                    
                    
                    
                    
                    unownedWaitingForSecond = True
                    for a in range(0, len(players)):
                        if players[a].doesTileBelongToPlayer(mainMap.grid[y][x].getID()):
                            unownedWaitingForSecond = False
                            break
                    
                    cost = popupText.render(f"Cost: {mainMap.grid[y][x].tileValue} Gold", True, (0, 0, 0))
                    goToManage = popupText.render(f"Manage Population", True, (0, 0, 0))
                    if isinstance(mainMap.grid[y][x], landTile):
                        goToUpgrade = popupText.render(f"Upgrade Tile", True, (0, 0, 0))
                        currentLevel = bigText.render(f"Level: {mainMap.grid[y][x].level}", True, (0, 0, 0))
                    production1 = popupText.render(f"{mainMap.grid[y][x].returnProduction1()}", True, (0, 0, 0))
                    production2 = popupText.render(f"{mainMap.grid[y][x].returnProduction2()}", True, (0, 0, 0))
                    civiliansTile = popupText.render(f"Civilians: {mainMap.grid[y][x].getCivLength()}", True, (0, 0, 0))
                    soldiersTile = popupText.render(f"Soldiers: {mainMap.grid[y][x].getSolLength()}", True, (0, 0, 0))
                    production1YPosition = 0
                    production2YPosition = 0
                    productionXposition = 0
                    costXPosition = 0
                    costYPosition = 0
                    goToManageYPosition = 0

                    tilePopup = False
                    if currentplayer.doesTileBelongToPlayer(mainMap.grid[y][x].getID()):
                       tilePopup = True                 
                       if mainMap.grid[y][x].getCol() < 25:
                            if mainMap.grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) + 25, (y * 25) + 25, 150, 150)
                                exitButton = pygame.Rect((x * 25) + 25, (y * 25) + 150, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) + 50, (y * 25) + 125, 100, 25)
                                if isinstance(mainMap.grid[y][x], landTile):
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
                                if isinstance(mainMap.grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) + 50, (y * 25) - 80, 100, 25)
                                productionXposition = x * 25 + 55
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 45
                                goToUpgradeYPosition = y * 25 - 75
                       else:
                            if mainMap.grid[y][x].getRow() < 15:
                                popuprect = pygame.Rect((x * 25) - 150, (y * 25) + 25, 150, 150)
                                exitButton = pygame.Rect((x * 25) - 150, (y * 25) + 150, 150, 25)
                                goToManageButton = pygame.Rect((x * 25) - 128, (y * 25) + 125, 100, 25)
                                if isinstance(mainMap.grid[y][x], landTile):
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
                                if isinstance(mainMap.grid[y][x], landTile):
                                    goToUpgradeButton = pygame.Rect((x * 25) - 128, (y * 25) - 80, 100, 25)
                                productionXposition = x * 25 - 123
                                production1YPosition = y * 25 - 120
                                production2YPosition = y * 25 - 135
                                civiliansTileYPosition = y * 25 - 107
                                soldiersTileYPosition = y * 25 - 93
                                goToManageYPosition = y * 25 - 45
                                goToUpgradeYPosition = y * 25 - 75

                    else:
                        if mainMap.grid[y][x].getCol() < 25:
                            if mainMap.grid[y][x].getRow() < 15:
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
                            if mainMap.grid[y][x].getRow() < 15:
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

                        mainMap.displayMap(screen1)
                        pygame.draw.rect(screen1, (211, 182, 131), popuprect)
                        pygame.draw.rect(screen1, (209, 27, 27), exitButton)
                        pygame.draw.rect(screen1, (255, 255, 255), goToManageButton)
                        if isinstance(mainMap.grid[y][x], landTile):
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
                                if  isinstance(mainMap.grid[y][x], landTile) and goToUpgradeButton.collidepoint(event.pos):
                                    isUpgradingTile = True
                                    exitButton = pygame.Rect(975, 225, 50, 50)
                                    upgradeTileButton = pygame.Rect(600, 300, 200, 50)
                                    clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 25 Brick", True, (0, 0, 0))
                                    if mainMap.grid[y][x].level == 1:
                                        clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 50 Brick", True, (0, 0, 0))
                                    elif mainMap.grid[y][x].level == 2:
                                        clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 100 Brick", True, (0, 0, 0))
                                    elif mainMap.grid[y][x].level == 3:
                                        clickToUpgradeTile = bigText.render(f"Tile Maxed Out", True, (0, 0, 0))
                                    while isUpgradingTile:
                                        mainMap.displayMap(screen1)                                       
                                        
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
                                                    if mainMap.grid[y][x].level == 0:
                                                        if currentplayer.getBrick() >= 25:
                                                            mainMap.grid[y][x].upgradeTile(currentplayer)
                                                            clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 50 Brick", True, (0, 0, 0))
                                                            pygame.display.update()
                                                    elif mainMap.grid[y][x].level == 1:
                                                        if currentplayer.getBrick() >= 50:
                                                            mainMap.grid[y][x].upgradeTile(currentplayer)
                                                            clickToUpgradeTile = bigText.render(f"Cost To Upgrade Tile: 100 Brick", True, (0, 0, 0))
                                                            pygame.display.update()
                                                    elif mainMap.grid[y][x].level == 2:
                                                        if currentplayer.getBrick() >= 100:
                                                            mainMap.grid[y][x].upgradeTile(currentplayer)
                                                            clickToUpgradeTile = bigText.render(f"Tile Maxed Out", True, (0, 0, 0))
                                                            pygame.display.update()
                                                    else:
                                                        break
                                                    
                                                    currentLevel = bigText.render(f"Level: {mainMap.grid[y][x].level}", True, (0, 0, 0))
                                                    screen1.blit(currentLevel, (250, 350))
                                                    
                                                    pygame.display.update() 
                                
                                if goToManageButton.collidepoint(event.pos):
                                    managePopulation(mainMap, screen1, y, x, bigText, managescreen)
                                    tilePopup = False                  
                                                        
                    while unownedWaitingForSecond:
                        
                        mainMap.displayMap(screen1)
                        

                        
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
                                    if currentplayer.getGold() >= mainMap.grid[y][x].tileValue:
                                        if currentplayer.checkExpandable(mainMap.grid[y][x].getID()):
                                            if not(len(currentplayer.territories) == 0 and isinstance(mainMap.grid[y][x], oceanTile)):
                                                currentplayer.subtractGold(mainMap.grid[y][x].tileValue)                           
                                                currentplayer.addTerritoryToPlayer(mainMap.grid[y][x].getID())
                                                if isinstance(mainMap.grid[y][x],landTile):
                                                    mainMap.grid[y][x].manuallyAddPopulation(1)
                                                currentplayer.totalPlayerPopulation(mainMap)
                                                currentplayer.updateFunctionalProductionValues(mainMap)
                                                currentplayer.updateProductionValues(mainMap)
                                            
                                            
                                if noExpand.collidepoint(event.pos):
                                    screen1.fill(Background_color)
                                unownedWaitingForSecond = False
                    
                    
                

                    


                            
        #player count display
        
        textdraw = text.render(f"Player: {currentplayer.name}", True, (0, 0, 0))
        textturnnumber = text.render(f"Turn #{turnnumber}", True, (0, 0, 0))
        screen1.blit(textdraw, (10, 760))
        screen1.blit(textturnnumber, (10, 810))

        for row in range(30):
            for col in range(50):
                mainMap.grid[row][col].draw(screen1)
                if tiley < 749:
                    screen1.blit(wowzer, (tilex, tiley))
        
        
        for a in range(0, len(players)):
            players[a].drawBorders(screen1)
            players[a].addBordering()
        
        #Resource display
        if resourcedisplay1:
            
            resourceViewSetup(screen1, text, "Resources:","Per Turn:", "Total:")
                
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
            currentplayer.updateFunctionalProductionValues(mainMap)
            currentplayer.updateProductionValues(mainMap)
            currentplayer.updateWoodUse(mainMap)
            foodPerTurn = text.render(f"{currentplayer.foodperturn - currentplayer.foodConsumption}", True, (0, 0, 0))
            screen1.blit(foodPerTurn, (675, 60))
            stonePerTurn = text.render(f"{currentplayer.stoneperturn}", True, (0, 0, 0))
            screen1.blit(stonePerTurn, (775, 60))
            woodPerTurn = text.render(f"{currentplayer.woodperturn - currentplayer.woodUse}", True, (0, 0, 0))
            screen1.blit(woodPerTurn, (875, 60))
                
        

        elif resourcedisplay2:
            #(must be elif, not if, just if causes the rectangular box to flicker)
            resourceViewSetup(screen1, text, "Resources:", "Found Last Turn:", "")

            treasureGold = text.render(f"{currentplayer.lastTurnGoldFromTreasure}", True, (0, 0, 0))
            screen1.blit(treasureGold, (475, 60))
            treasureBrick = text.render(f"{currentplayer.lastTurnBrickFromTreasure}", True, (0, 0, 0))
            screen1.blit(treasureBrick, (575, 60))
            treasureFood = text.render(f"{currentplayer.lastTurnFoodFromTreasure}", True, (0, 0, 0))
            screen1.blit(treasureFood, (675, 60))
            treasureStone = text.render(f"{currentplayer.lastTurnStoneFromTreasure}", True, (0, 0, 0))
            screen1.blit(treasureStone, (775, 60))
            treasureWood = text.render(f"{currentplayer.lastTurnWoodFromTreasure}", True, (0, 0, 0))
            screen1.blit(treasureWood, (875, 60))
        
        pygame.display.update()
    
    screen2 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while civview:
        mainMap.displayMap(screen2)
        pygame.draw.rect(screen2, (211, 182, 131), backgroundUI)
        move.displayNumOfTypePerTile(screen2, "civilian", mainMap, players, currentplayerindex, currentplayer, text3)
        pygame.draw.rect(screen2, (29, 158, 29), populationview)
        pygame.draw.rect(screen2, (114, 9, 219), movePopButtonMode)
        popOnOrOff = text.render(("Move:"), True, (255, 255, 255))
        if movePopMode == False:
            #print(0) 
            pygame.draw.rect(screen2, (255, 0, 0), moveMode)
        else:
            #print(1)
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
                    popcivilians = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getCivLength()}", True, (255, 255, 255))
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
                                            if isinstance(mainMap.grid[tilerow1][tilecol1], landTile):
                                                if ((len(mainMap.grid[tilerow1][tilecol1].population)) > 1 and currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID())):
                                                    mainMap.grid[tilerow1][tilecol1].population[mainMap.grid[tilerow1][tilecol1].findIndexOfType("civilian")].movePopulation(mainMap.grid[tilerow1][tilecol1].findIndexOfType("civilian"), tilerow1, tilecol1, tilerow2, tilecol2, mainMap.grid)
                                            else:
                                                if ((len(mainMap.grid[tilerow1][tilecol1].population)) > 0 and currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID())):
                                                    mainMap.grid[tilerow1][tilecol1].population[mainMap.grid[tilerow1][tilecol1].findIndexOfType("civilian")].movePopulation(mainMap.grid[tilerow1][tilecol1].findIndexOfType("civilian"), tilerow1, tilecol1, tilerow2, tilecol2, mainMap.grid)
                                            waitingforclick = False
                                            waitingforclick2 = False
                        elif movePopButtonMode.collidepoint(event.pos):
                            movePopMode = False
                            waitingforclick = False
                        
                

            
       
    screen3 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    #  = pygame.Rect(1050, 750, 100, 100)              
    while battleview:
        mainMap.displayMap(screen3)
        pygame.draw.rect(screen3, (211, 182, 131), backgroundUI)
        move.displayNumOfTypePerTile(screen3, "soldier", mainMap, players, currentplayerindex, currentplayer, text3)
        pygame.draw.rect(screen3, (139, 124, 124), militaryview)
        pygame.draw.rect(screen3, (114, 9, 219), movePopButtonMode)
        popOnOrOff = text.render(("Move:"), True, (255, 255, 255))
        if movePopMode == False:
            #print(0)
            pygame.draw.rect(screen3, (255, 0, 0), moveMode)
        else:
            #print(1)
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
            mainMap.displayMap(screen3)
            for a in range(0, len(players)):
                players[a].drawBorders(screen3)
                players[a].addBordering()
                if not a == currentplayerindex:
                    for b in range(0, len(players[a].territories)):
                        for c in range(0, len(currentplayer.territories)):
                            if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True:
                                temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                                pygame.draw.rect(screen3, (211, 182, 131), temprect)
                                popsoldiers = text3.render(f"{mainMap.grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].getSolLength()}", True, (255, 255, 255))
                                screen3.blit(popsoldiers, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
            for a in range(0, len(currentplayer.territories)):
                temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                pygame.draw.rect(screen3, (211, 182, 131), temprect)
                popsoldiers = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getSolLength()}", True, (255, 255, 255))
                screen3.blit(popsoldiers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
            currentplayer.drawBorders(screen3)
            waitingforclick = True
            while waitingforclick:
                for a in range(0, len(currentplayer.territories)):
                    temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                    pygame.draw.rect(screen3, (211, 182, 131), temprect)
                    popsoldiers = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getSolLength()}", True, (255, 255, 255))
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
                                            if isinstance(mainMap.grid[tilerow1][tilecol1], landTile):
                                                if ((len(mainMap.grid[tilerow1][tilecol1].population)) > 1 and currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID())):
                                                    mainMap.grid[tilerow1][tilecol1].population[mainMap.grid[tilerow1][tilecol1].findIndexOfType("soldier")].movePopulation(mainMap.grid[tilerow1][tilecol1].findIndexOfType("soldier"), tilerow1, tilecol1, tilerow2, tilecol2, mainMap.grid)
                                                if (not(currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID()))) and checkPureAdjacency(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID()):
                                                    print("got through")
                                                    #check if both tiles are owned, if both are land, and if the attacking player has enough population to invade
                                                    if mainMap.istileowned(tilecol2, tilerow2, players, numplayers) and (len(mainMap.grid[tilerow1][tilecol1].population)) > 1:    
                                                        if isinstance(mainMap.grid[tilerow2][tilecol2], landTile):
                                                            print("LAND BATTLE TIME")
                                                            #the actual battle square here
                                                            #comment out battle screen for now
                                                            actualBattle(currentplayer, players[findPlayerFromTile(mainMap.grid[tilerow2][tilecol2].getID(), players)], mainMap.grid[tilerow1][tilecol1].getSolLength(), mainMap.grid[tilerow2][tilecol2].getSolLength(), mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID(), mainMap.grid)
                                                        else:
                                                            actualBattle(currentplayer, players[findPlayerFromTile(mainMap.grid[tilerow2][tilecol2].getID(), players)], mainMap.grid[tilerow1][tilecol1].getSolLength(), mainMap.grid[tilerow2][tilecol2].getSolLength(), mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID(), mainMap.grid)
                                                            print("Land to water")
                                                        mainMap.displayMap(screen3)
                                                        for a in range(0, len(players)):
                                                            players[a].addBordering()
                                                            players[a].drawBorders(screen3)
                                                            
                                                        pygame.display.flip()
                                            else:
                                                if ((len(mainMap.grid[tilerow1][tilecol1].population)) > 0 and currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID())):
                                                    mainMap.grid[tilerow1][tilecol1].population[mainMap.grid[tilerow1][tilecol1].findIndexOfType("soldier")].movePopulation(mainMap.grid[tilerow1][tilecol1].findIndexOfType("soldier"), tilerow1, tilecol1, tilerow2, tilecol2, mainMap.grid)
                                                if (not(currentplayer.checkAdjacencyForMovement(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID()))) and checkPureAdjacency(mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID()):
                                                    print("got through")
                                                    if mainMap.istileowned(tilecol2, tilerow2, players, numplayers) and (len(mainMap.grid[tilerow1][tilecol1].population)) > 0:
                                                        if isinstance(mainMap.grid[tilerow2][tilecol2], landTile):
                                                            actualBattle(currentplayer, players[findPlayerFromTile(mainMap.grid[tilerow2][tilecol2].getID(), players)], mainMap.grid[tilerow1][tilecol1].getSolLength(), mainMap.grid[tilerow2][tilecol2].getSolLength(), mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID(), mainMap.grid)  
                                                            print("AMPHIBIOUS ATTACK")
                                                        else:
                                                            actualBattle(currentplayer, players[findPlayerFromTile(mainMap.grid[tilerow2][tilecol2].getID(), players)], mainMap.grid[tilerow1][tilecol1].getSolLength(), mainMap.grid[tilerow2][tilecol2].getSolLength(), mainMap.grid[tilerow1][tilecol1].getID(), mainMap.grid[tilerow2][tilecol2].getID(), mainMap.grid)
                                                            print("NAVAL BATTLE")  
                                                            #maybe do something more with these in the future?
                                                        mainMap.displayMap(screen3)
                                                        for a in range(0, len(players)):
                                                            players[a].addBordering()
                                                            players[a].drawBorders(screen3)
                                                        pygame.display.flip()
                                            waitingforclick = False
                                            waitingforclick2 = False
                        elif movePopButtonMode.collidepoint(event.pos):
                            movePopMode = False
                            waitingforclick = False

    screen4 = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    while levelView:                        
        mainMap.displayMap(screen4)
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
                        if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True and isinstance(mainMap.grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50], landTile):
                            print("4")
                            temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                            pygame.draw.rect(screen4, (211, 182, 131), temprect)
                            level = text3.render(f"{mainMap.grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].level}", True, (255, 255, 255))
                            screen4.blit(level, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
        for a in range(0, len(currentplayer.territories)):
            #only make rectangles for land tiles (for currentplayer)
            if isinstance(mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50], landTile):
                temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
                pygame.draw.rect(screen4, (211, 182, 131), temprect)
                level = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].level}", True, (255, 255, 255))
                screen4.blit(level, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen4)
        pygame.draw.rect(screen1, (255, 0, 0), tileLevelView)
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tileLevelView.collidepoint(event.pos):
                    levelView = False
                    running1 = True
        pygame.display.flip()



