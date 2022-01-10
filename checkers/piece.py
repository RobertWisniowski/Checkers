from .properties import *

font = pygame.font.SysFont("Arial", 30)

class Piece:
    def __init__(self, color, row, column):
        self.color = color
        self.row = row
        self.column = column
        self.king = False

        if self.color == RED:
            self.course = 1
        else:
            self.course = -1

        self.x = 0
        self.y = 0
        self.position()

    def position(self):
        self.x = SQUARE * self.column + SQUARE // 2
        self.y = SQUARE * self.row + SQUARE // 2

    def create_king(self):
        self.king = True

    def draw(self, window):
        rad = SQUARE // 2 - self.GROUND
        pygame.draw.circle(window, self.color, (self.x, self.y), rad)
        text = font.render("C", True, self.color)
        window.blit (text, (window, self.x, self.y))

    def __repr__(self):
        return str(self.color)

