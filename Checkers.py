import pygame
pygame.init()
from checkers.properties import *
from checkers.checkerboard import *
from checkers.piece import*
import sys

gameIsOver = False
winner ='None'
redPiecesCount = 12
whitePiecesCount = 12


def highlight(ClickedNode, Grid, OldHighlight):
    Column,Row = ClickedNode
    Grid[Column][Row].colour=ORANGE
    if OldHighlight:
        resetColours(Grid, OldHighlight)

    HighlightpotentialMoves(ClickedNode, Grid)
    return (Column,Row)


def make_grid(rows, width):
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
            elif(abs(i+j)%2==0) and i>4:
                node.piece = Man('W')
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

def main(WIDTH, ROWS):
    grid = make_grid(ROWS, WIDTH)
    highlightedPiece = None
    currMove = 'W'
    global redPiecesCount
    global whitePiecesCount
    global gameIsOver
    global winner
    info = font.render("Aby zresetować grę naciśnij dowolny przycisk na klawiaturze.", True, RED)
    WIN.blit (info, (50, 830))
    


    while True:

        if gameIsOver == True:
            currMove = 'None'
            if winner == 'R':
                WIN.blit (REDWIN, (50, 870))
            elif winner == 'W':
                WIN.blit (WHITEWIN, (50, 870))
            grid = make_grid(ROWS, WIDTH)
        
        if currMove == 'W':
                WIN.blit (WHITETURN, (50, 870))
        elif currMove == 'R':
                WIN.blit (REDTURN, (50, 870))
        else:
            currMove = "None"

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                whitePiecesCount = 12
                redPiecesCount = 12
                gameIsOver == False
                winner = "None"
                grid = make_grid(ROWS, WIDTH)
                highlightedPiece = None
                currMove = 'W'
                WIN.blit (WHITETURN, (50, 870))

            if event.type == pygame.MOUSEBUTTONDOWN:
                clickedNode = getNode(grid, ROWS, WIDTH)
                ClickedPositionColumn, ClickedPositionRow = clickedNode
                if grid[ClickedPositionColumn][ClickedPositionRow].colour == BLUE:
                    if highlightedPiece:
                        pieceColumn, pieceRow = highlightedPiece
                    if currMove == grid[pieceColumn][pieceRow].piece.team:
                        resetColours(grid, highlightedPiece)
                        currMove=move(grid, highlightedPiece, clickedNode)
                elif highlightedPiece == clickedNode:
                    pass
                else:
                    if grid[ClickedPositionColumn][ClickedPositionRow].piece:
                        if currMove == grid[ClickedPositionColumn][ClickedPositionRow].piece.team:
                            highlightedPiece = highlight(clickedNode, grid, highlightedPiece)


        update_display(WIN, grid,ROWS,WIDTH)


main(WIDTH, ROWS)