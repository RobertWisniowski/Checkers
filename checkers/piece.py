import pygame
pygame.init()
from .properties import *

class Piece:
    def __init__(self, team):
        self.team=team
        self.image= REDPIECE if self.team=='R' else WHITEPIECE
        self.type=None

    def draw(self, x, y):
        WIN.blit(self.image, (x,y))


def getNode(grid, rows, width):
    gap = width//rows
    RowX,RowY = pygame.mouse.get_pos()
    Row = RowX//gap
    Col = RowY//gap
    return (Col,Row)






