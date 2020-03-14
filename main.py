import sys, pygame
from racket import racket
from ball import ball

pygame.init()

size = width, height = 800, 500
BLACK = (0,0,0)
BLUE = (0,0,255)
RED = (255,0,0)
WHITE = (255,255,255)
screen = pygame.display.set_mode(size)

def render():
    screen.fill(BLACK)
    player1.drawRacket()
    player2.drawRacket()
    ball.drawBall()

if __name__ == "__main__":
    player1 = racket(screen, BLUE, 1, size)
    player2 = racket(screen, RED, 2, size)
    ball = ball(screen, WHITE, size)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
        
        keys=pygame.key.get_pressed()
        if keys:
            player1.movement(keys)
            player2.movement(keys)
        ball.ballMovement()    
        render()
        pygame.display.update()
    
    
    