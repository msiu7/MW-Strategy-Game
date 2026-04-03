import pygame

def managePopulation(map, screen, y, x, bigText, managescreen):
    while(True):    
        for row in range(30):
            for col in range(50):
                map.grid[row][col].draw(screen)
        unemployedTile = bigText.render(f"Unemployed: {map.grid[y][x].getUnemployedLength()}", True, (0, 0, 0))
        civiliansTile = bigText.render(f"Civilians: {map.grid[y][x].getCivLength()}", True, (0, 0, 0))
        soldiersTile = bigText.render(f"Soldiers: {map.grid[y][x].getSolLength()}", True, (0, 0, 0))
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
                    if map.grid[y][x].getSolLength() > 0:  
                        map.grid[y][x].population[map.grid[y][x].findIndexOfType("soldier")].changeType("civilian")
                        print(f"Civ: {map.grid[y][x].getCivLength()}")
                        print(f"Sol:{map.grid[y][x].getSolLength()}")
                        print(f"Un:{map.grid[y][x].getUnemployedLength()}")
                if civtosol.collidepoint(event.pos):
                    if map.grid[y][x].getCivLength() > 0:
                        map.grid[y][x].population[map.grid[y][x].findIndexOfType("civilian")].changeType("soldier")
                        print(f"Civ: {map.grid[y][x].getCivLength()}")
                        print(f"Sol:{map.grid[y][x].getSolLength()}")
                        print(f"Un:{map.grid[y][x].getUnemployedLength()}")