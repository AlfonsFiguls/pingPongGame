import pygame
import random

class ball():

    def __init__(self, screen, color, screenSize):
        self.screen = screen
        self.color = color
        self.screenSize = screenSize
        self.ballPos = (400,random.randint(100,300))
        self.ballWidth = 18
        self.direction = [1 if random.randint(-1,1) >=1 else -1, 1 if random.randint(-1,1) >=1 else -1]
        self.speed = 3
    
    def drawBall(self):
        pygame.draw.circle(self.screen, self.color, self.ballPos, self.ballWidth)
    
    def checkTopBottomLimits(self):
        if self.ballPos[1] + self.ballWidth >= self.screenSize[1] or self.ballPos[1] - self.ballWidth <= 0:
            self.direction = [self.direction[0],self.direction[1]*(-1)]
        
        if self.ballPos[0] + self.ballWidth >= self.screenSize[0] or self.ballPos[0] - self.ballWidth <= 0:
            self.direction = [self.direction[0]*(-1),self.direction[1]]
        
    def ballMovement(self):
        self.checkTopBottomLimits()
        self.ballPos = (self.ballPos[0]+self.direction[0]*self.speed, self.ballPos[1]+self.direction[1]*self.speed)