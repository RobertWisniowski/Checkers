from asyncio.windows_events import NULL
import pygame
pygame.init()
from .properties import *
from .piece import*

pygame.init()
pygame.display.set_caption('Checkers')

redPiecesCount = 12
whitePiecesCount = 12
gameIsOver = False
winner ='None'

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.colour = WHITE
        self.piece = None
        self.piecesWhite = 12
        self.piecesRed = 12

    def draw(self, WIN):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, WIDTH / ROWS, WIDTH / ROWS))
        if self.piece:
            WIN.blit(self.piece.image, (self.x, self.y))
    def help(self):
        print("Klasa przechowuje informacje odpowiedzialne za definiowanie rozmiaru planszy, ilości pionków na początku rozgrywki, koloru pól \"białych\", a także szerokości i wysokości planszy. Prócz tego zawiera metodę draw(), która rysuje kwadratowe pola na planszy.")
def generatePotentialMoves(nodePosition, grid):
    checker = lambda x,y: x+y>=0 and x+y<8
    positions= []
    column, row = nodePosition
    if grid[column][row].piece:
        if grid[column][row].piece.team == "R":
            grid[column][row].piece.image = REDPIECECHOOSEN
            vectors = [[1, -1], [1, 1]] 
        else:
            vectors = [[-1, -1], [-1, 1]]
            grid[column][row].piece.image = WHITEPIECECHOOSEN
        if grid[column][row].piece.type=='KING':
            if grid[column][row].piece.team =='R':
                grid[column][row].piece.image = REDKINGCHOOSEN
            else:
                grid[column][row].piece.image = WHITEKINGCHOOSEN
            vectors = [[1, -1], [1, 1],[-1, -1], [-1, 1]]
        for vector in vectors:
            columnVector, rowVector = vector
            if checker(columnVector,column) and checker(rowVector,row):
                #grid[(column+columnVector)][(row+rowVector)].colour=ORANGE
                if not grid[(column+columnVector)][(row+rowVector)].piece:
                    positions.append((column + columnVector, row + rowVector))
                elif grid[column+columnVector][row+rowVector].piece and\
                        grid[column+columnVector][row+rowVector].piece.team==opposite(grid[column][row].piece.team):

                    if checker((2* columnVector), column) and checker((2* rowVector), row) \
                            and not grid[(2* columnVector)+ column][(2* rowVector) + row].piece:
                        positions.append((2* columnVector+ column,2* rowVector+ row ))

    return positions

def highlightpotentialMoves(piecePosition, grid):
    positions = generatePotentialMoves(piecePosition, grid)
    for position in positions:
        Column,Row = position
        grid[Column][Row].colour=BLUE

def opposite(team):
    return "R" if team=="W" else "W"

def resetColours(grid, node):
    positions = generatePotentialMoves(node, grid)
    positions.append(node)

    for colouredNodes in positions:
        nodeX, nodeY = colouredNodes
        grid[nodeX][nodeY].colour = BLACK if abs(nodeX - nodeY) % 2 == 0 else WHITE
    
def updateDisplay(win, grid, rows, width):
    for row in grid:
        for spot in row:
            spot.draw(win)
    drawGrid(win, rows, width)
    pygame.display.update()


def drawGrid(win, rows, width):
    gap = width // ROWS
    for i in range(rows):
        pygame.draw.line(win, BLACK, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))

def highlight(ClickedNode, Grid, OldHighlight):
    Column,Row = ClickedNode
    Grid[Column][Row].colour=ORANGE
    if OldHighlight:
        resetColours(Grid, OldHighlight)
    highlightpotentialMoves(ClickedNode, Grid)
    return (Column,Row)


def makeGrid(rows, width):
    grid = []
    gap = width// rows
    count = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j,i, gap)
            if abs(i-j) % 2 == 0:
                node.colour=BLACK
            if (abs(i+j)%2==0) and (i<3):
                node.piece = Man('R')
                #print(i, j, node.piece.team)
            elif(abs(i+j)%2==0) and i>4:
                node.piece = Man('W')
                #print(i, j, node.piece.team)
            count+=1
            grid[i].append(node)
    return grid

def getNode(grid, rows, width):
    gap = width//rows
    RowX,RowY = pygame.mouse.get_pos()
    Row = RowX//gap
    Col = RowY//gap
    return (Col,Row)

def gameOver(grid,newColumn, newRow):
    global gameIsOver
    gameIsOver = True
    global winner
    winner = grid[newColumn][newRow].piece.team

def move(grid, piecePosition, newPosition):
    global redPiecesCount
    global whitePiecesCount
    resetColours(grid, piecePosition)
    newColumn, newRow = newPosition
    oldColumn, oldRow = piecePosition

    piece = grid[oldColumn][oldRow].piece
    grid[newColumn][newRow].piece=piece
    grid[newColumn][newRow].piece.resetImage()
    grid[oldColumn][oldRow].piece = None

    if newColumn==7 and grid[newColumn][newRow].piece.team=='R':
        grid[newColumn][newRow].piece = King('R')
    if newColumn==0 and grid[newColumn][newRow].piece.team=='W':
        grid[newColumn][newRow].piece = King('W')

    if abs(newColumn-oldColumn)==2 or abs(newRow-oldRow)==2:
        grid[int((newColumn+oldColumn)/2)][int((newRow+oldRow)/2)].piece = None
        if grid[newColumn][newRow].piece.team=='R':
            whitePiecesCount -= 1
        else:

            redPiecesCount -= 1
        if redPiecesCount == 0 or whitePiecesCount == 0:
            gameOver(grid,newColumn, newRow)
        return grid[newColumn][newRow].piece.team
    return opposite(grid[newColumn][newRow].piece.team)
            
def resetPieces():
    global redPiecesCount
    global whitePiecesCount
    global winner
    global gameIsOver
    gameIsOver = False
    winner = "None"
    redPiecesCount = 12
    whitePiecesCount = 12

def changePiecesCount(red, white):
    global redPiecesCount
    global whitePiecesCount 
    redPiecesCount = red
    whitePiecesCount = white

def showWinner():
    global winner
    return winner

def showIfGameIsOver():
    global gameIsOver
    return gameIsOver



    