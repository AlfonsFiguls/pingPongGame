import pygame
import random

class ball():

    def __init__(self, screen, color, screenSize):
        self.screen = screen
        self.color = color
        self.screenSize = screenSize
        self.ballPos = (400,random.randint(100,300))
        self.ballWidth = 20
        self.direction = [1 if random.randint(-1,1) >=1 else -1, 1 if random.randint(-1,1) >=1 else -1]
        self.speed = 8
    
    def drawBall(self):
        pygame.draw.circle(self.screen, self.color, self.ballPos, self.ballWidth)
    
    def checkTopBottomLimits(self):
        if self.ballPos[1] + self.ballWidth >= self.screenSize[1] or self.ballPos[1] - self.ballWidth <= 0:
            self.direction = [self.direction[0],self.direction[1]*(-1)]
    
    def checkRacketLimits(self, player1, player2):
        if self.ballPos[0] - self.ballWidth <= 50 and self.ballPos[1] in range(player1[1],player1[1]+180) and self.direction[0] == -1: #50 is player1 racket final pos in x axis. 180 is the racket length.
            self.direction = [self.direction[0]*(-1),self.direction[1]]
        if self.ballPos[0] + self.ballWidth >= self.screenSize[0] - 50 and self.ballPos[1] in range(player2[1],player2[1]+180) and self.direction[0] == 1:
            self.direction = [self.direction[0]*(-1),self.direction[1]]
    
    def checkPointScored(self):
        if self.ballPos[0] + self.ballWidth >= self.screenSize[0] or self.ballPos[0] - self.ballWidth <= 0:
            return True

    def ballMovement(self, player1, player2):
        self.checkTopBottomLimits()
        self.checkRacketLimits(player1, player2)
        if (self.checkPointScored()):
            return True
        self.ballPos = (self.ballPos[0]+self.direction[0]*self.speed, self.ballPos[1]+self.direction[1]*self.speed)
    
    def resetPos(self):
        self.ballPos = (400,random.randint(100,300))