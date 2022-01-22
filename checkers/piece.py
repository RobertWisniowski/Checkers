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

    def help(self):
        print("Klasa przechowuje podstawowe informacje o pionku. Zawiera w sobie również metodę draw() odpowiedzialną za rysowanie pionka na szachownicy i metodę resetImage(), która przywraca domyślną teksturę pionka po wykonaniu ruchu.")

class King(Piece):
    def __init__(self, team):
        self.team=team
        self.image = REDKING if self.team =='R' else WHITEKING
        self.type='KING'

    def resetImage(self):
        self.image = REDKING if self.team =='R' else WHITEKING

    def help(self):
        print("Klasa dziedzicząca po klasie Piece. Nadpisuje wartości w niej zawarte. Prócz tego, nadpisuje metodę resetImage(), by odpowiadała innemu wizerunkowi damki na szachownicy")

class Man(Piece):
    def __init__(self, team):
        self.team=team
        self.image = REDPIECE if self.team =='R' else WHITEPIECE
        self.type=None   
    def help(self):
        print("Klasa dziedzicząca po klasie Piece. Nadpisuje wartości w niej zawarte.")


