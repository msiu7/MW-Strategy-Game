import pygame

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