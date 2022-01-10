import pygame
from .properties import *

class Checkerboard:
    def __init__(self):
        self.checkerboard = []
        self.selected_piece = None
        self.black_alive = 12
        self.white_alive = 12
        self.black_kings_alive = 0
        self.white_kings_alive = 0

    def board(self):
        pass

    def fields(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for column in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, WHITE, (column * SQUARE, row * SQUARE, SQUARE, SQUARE) )