import pygame


WIDTH = 800
HEIGHT = 950
ROWS = 8

REDPIECE= pygame.image.load('red.png')
WHITEPIECE= pygame.image.load('white.png')
REDPIECECHOOSEN= pygame.image.load('redChoosen.png')
WHITEPIECECHOOSEN= pygame.image.load('whiteChoosen.png')

REDKING = pygame.image.load('redKing.png')
WHITEKING = pygame.image.load('whiteKing.png')
REDKINGCHOOSEN = pygame.image.load('redKingChoosen.png')
WHITEKINGCHOOSEN = pygame.image.load('whiteKingChoosen.png')

PROHIBITEDMOVE = pygame.image.load('prohibitedMove.png')
ALLOWEDDMOVE = pygame.image.load('allowedMove.png')

WHITETURN = pygame.image.load('whiteTurn.png')
REDTURN = pygame.image.load('redTurn.png')

WHITEWIN = pygame.image.load('whiteWin.png')
REDWIN = pygame.image.load('redWin.png')

WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (235, 168, 52)
BLUE = (76, 252, 241)
RED = (255, 0, 0)

WIN = pygame.display.set_mode((WIDTH,HEIGHT))

font = pygame.font.SysFont(None, 30)