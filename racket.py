import pygame

class racket():
    
    def __init__(self, screen, color, player, screenSize):
        self.screen = screen
        self.color = color
        iniXPos = 20 if player == 1 else 750
        self.rect = pygame.draw.rect(screen,color,(iniXPos,160,30,180))
        self.keyUP = pygame.K_w if player == 1 else pygame.K_UP
        self.keyDOWN = pygame.K_s if player == 1 else pygame.K_DOWN
        self.screenSize = screenSize
    
    def drawRacket(self):
        pygame.draw.rect(self.screen,self.color,self.rect)
    
    def movement(self, keys):
        if keys[self.keyUP] and self.rect[1] > 0:
            self.rect.move_ip(0, -10)
        if keys[self.keyDOWN] and self.rect[1] < self.screenSize[1] - 180:
            self.rect.move_ip(0, 10)
            

        