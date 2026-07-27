import pygame

class displays:

    @staticmethod
    def resourceViewSetup(screen, text, s1, s2, s3):
        #popupText = pygame.font.SysFont("Arial", 10)
        resourcedisplay = pygame.Rect(200, 25, 850, 100)
        pygame.draw.rect(screen, (211, 182, 131), resourcedisplay)
        #Icons/Labels
        resourcesLabel = text.render(s1, True, (0, 0, 0))
        screen.blit(resourcesLabel, (250, 30))
        perTurnLabel = text.render(s2, True, (0, 0, 0))
        screen.blit(perTurnLabel, (250, 60))
        totalLabel = text.render(s3, True, (0, 0, 0))
        screen.blit(totalLabel, (250, 90))
        goldIcon = text.render(f"Gold", True, (0, 0, 0))
        screen.blit(goldIcon, (475, 30))
        brickIcon = text.render(f"Brick", True, (0, 0, 0))
        screen.blit(brickIcon, (575, 30))
        foodIcon = text.render(f"Food", True, (0, 0, 0))
        screen.blit(foodIcon, (675, 30))
        stoneIcon = text.render(f"Stone", True, (0, 0, 0))
        screen.blit(stoneIcon, (775, 30))
        woodIcon = text.render(f"Wood", True, (0, 0, 0))
        screen.blit(woodIcon, (875, 30))

    @staticmethod
    def makeScoreboard(screen, numplayers, text):
        scoredisplay = pygame.Rect(200, 25, 300, 50 + 35 * numplayers)
        pygame.draw.rect(screen, (211, 182, 131), scoredisplay)
        scoreLabel = text.render("Score:", True, (0, 0, 0))
        screen.blit(scoreLabel, (350, 30))

    @staticmethod
    def managePopulation(map, screen, y, x, bigText, managescreen, currentplayer):
        while(True):    
            for row in range(30):
                for col in range(50):
                    map.grid[row][col].draw(screen)
            customText = pygame.font.SysFont("Arial", 20)
            unemployedTile = bigText.render(f"Unemployed: {map.grid[y][x].getUnemployedLength()}", True, (0, 0, 0))
            civiliansTile = bigText.render(f"Civilians: {map.grid[y][x].getCivLength()}", True, (0, 0, 0))
            soldiersTile = bigText.render(f"Soldiers: {map.grid[y][x].getSolLength()}", True, (0, 0, 0))
            poptocivText = customText.render("Convert to Civilian", True, (0, 0, 0))
            poptosolText = customText.render("Convert to Soldier", True, (0, 0, 0))
            soltocivText = customText.render("Convert to Civilian", True, (0, 0, 0))
            civtosolText = customText.render("Convert to Soldier", True, (0, 0, 0))
            exitButton = pygame.Rect(975, 225, 50, 50)
            pygame.draw.rect(screen, (211, 182, 131), managescreen)
            screen.blit(civiliansTile, (235, 230))
            screen.blit(soldiersTile, (235, 355))
            screen.blit(unemployedTile, (235, 470))
            poptociv = pygame.Rect(495, 465, 200, 50)
            poptosol = pygame.Rect(715, 465, 200, 50)
            soltociv = pygame.Rect(600, 355, 200, 50)
            civtosol = pygame.Rect(600, 230, 200, 50)
            pygame.draw.rect(screen, (255, 0, 0), exitButton)
            pygame.draw.rect(screen, (255, 255, 255), poptociv)
            pygame.draw.rect(screen, (255, 255, 255), poptosol)
            pygame.draw.rect(screen, (255, 255, 255), soltociv)
            pygame.draw.rect(screen, (255, 255, 255), civtosol)
            screen.blit(poptocivText, (525, 475))
            screen.blit(poptosolText, (745, 475))
            screen.blit(soltocivText, (630, 365))
            screen.blit(civtosolText, (630, 240))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exitButton.collidepoint(event.pos):
                        return
                    if poptociv.collidepoint(event.pos):
                        if map.grid[y][x].getUnemployedLength() > 0:
                            map.grid[y][x].population[map.grid[y][x].findIndexOfType("unemployed")].changeType("civilian")
                            print(f"Civ: {map.grid[y][x].getCivLength()}")
                            print(f"Sol:{map.grid[y][x].getSolLength()}")
                            print(f"Un:{map.grid[y][x].getUnemployedLength()}")
                    if poptosol.collidepoint(event.pos):
                        if map.grid[y][x].getUnemployedLength() > 0:
                            map.grid[y][x].population[map.grid[y][x].findIndexOfType("unemployed")].changeType("soldier")
                            print(f"Civ: {map.grid[y][x].getCivLength()}")
                            print(f"Sol:{map.grid[y][x].getSolLength()}")
                            print(f"Un:{map.grid[y][x].getUnemployedLength()}")           
                    if soltociv.collidepoint(event.pos):
                        if map.grid[y][x].getSolLength() > 0 and currentplayer.getStone() > 0:  
                            map.grid[y][x].population[map.grid[y][x].findIndexOfType("soldier")].changeType("civilian")
                            currentplayer.stone -= 1
                            print(f"Civ: {map.grid[y][x].getCivLength()}")
                            print(f"Sol:{map.grid[y][x].getSolLength()}")
                            print(f"Un:{map.grid[y][x].getUnemployedLength()}")
                    if civtosol.collidepoint(event.pos):
                        if map.grid[y][x].getCivLength() > 0 and currentplayer.getStone() > 0:
                            map.grid[y][x].population[map.grid[y][x].findIndexOfType("civilian")].changeType("soldier")
                            currentplayer.stone -= 1
                            print(f"Civ: {map.grid[y][x].getCivLength()}")
                            print(f"Sol:{map.grid[y][x].getSolLength()}")
                            print(f"Un:{map.grid[y][x].getUnemployedLength()}")