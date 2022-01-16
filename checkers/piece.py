import pygame
pygame.init()
from .properties import *

class Piece:
    def __init__(self, team):
        self.team=team
        self.image = None
        self.type=None

    def draw(self, x, y):
        WIN.blit(self.image, (x,y))

    def resetImage(self):
        self.image = REDPIECE if self.team =='R' else WHITEPIECE





class King(Piece):
    def __init__(self, team):
        self.team=team
        self.image = REDKING if self.team =='R' else WHITEKING
        self.type='KING'

    def resetImage(self):
        self.image = REDKING if self.team =='R' else WHITEKING

class Man(Piece):
    def __init__(self, team):
        self.team=team
        self.image = REDPIECE if self.team =='R' else WHITEPIECE
        self.type=None   



