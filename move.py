import pygame
from functions import checkPureAdjacency

class move():

    @staticmethod
    def displayNumOfTypePerTile(screen, civOrSol, mainMap, players, currentplayerindex, currentplayer, text3):
        for a in range(0, len(players)):
            players[a].drawBorders(screen)
            players[a].addBordering()
            if not a == currentplayerindex:
                for b in range(0, len(players[a].territories)):
                    for c in range(0, len(currentplayer.territories)):
                        if checkPureAdjacency(players[a].territories[b], currentplayer.territories[c]) == True:
                            print("drawrect")
                            temprect = pygame.Rect(((players[a].territories[b]) % 50) * 25 + 5, ((players[a].territories[b]) // 50) * 25 + 5, 15, 15)
                            pygame.draw.rect(screen, (211, 182, 131), temprect)
                            if(civOrSol == "civilian"):
                                popnumbers = text3.render(f"{mainMap.grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].getCivLength()}", True, (255, 255, 255))
                            else:
                                popnumbers = text3.render(f"{mainMap.grid[(players[a].territories[b]) // 50][(players[a].territories[b]) % 50].getSolLength()}", True, (255, 255, 255))
                            screen.blit(popnumbers, ((((players[a].territories[b]) % 50) * 25) + 10, ((players[a].territories[b]) // 50) * 25 + 5))    
        for a in range(0, len(currentplayer.territories)):
            temprect = pygame.Rect(((currentplayer.territories[a]) % 50) * 25 + 5, ((currentplayer.territories[a]) // 50) * 25 + 5, 15, 15)
            pygame.draw.rect(screen, (211, 182, 131), temprect)
            print("drawingrectself")
            if(civOrSol == "civilian"):
                popnumbers = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getCivLength()}", True, (255, 255, 255))
            else:
                popnumbers = text3.render(f"{mainMap.grid[(currentplayer.territories[a]) // 50][(currentplayer.territories[a]) % 50].getSolLength()}", True, (255, 255, 255))
            screen.blit(popnumbers, ((((currentplayer.territories[a]) % 50) * 25) + 10, ((currentplayer.territories[a]) // 50) * 25 + 5))
        currentplayer.drawBorders(screen)
