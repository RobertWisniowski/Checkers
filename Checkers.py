import pygame
from checkers.properties import *
from checkers.checkerboard import *

WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def main():
    gameStarted = True
    deltaTime = pygame.time.Clock()
    checkerboard = Checkerboard()

    while gameStarted:
        deltaTime.tick(FPS)

        for movement in pygame.event.get():
            if movement.type == pygame.QUIT:
                gameStarted = False

            if movement.type == pygame.MOUSEBUTTONDOWN:
                pass

        checkerboard.fields(WINDOW)
        pygame.display.update()
    
    pygame.quit()

main()