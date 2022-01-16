import pygame
pygame.init()
from checkers.properties import *
from checkers.checkerboard import *

def testFirstFourMoves():

    grid = make_grid(ROWS, WIDTH)
    currMove = 'W'
    highlightedPiece = None

    rows = (5, 4, 2, 3, 5, 4, 2, 3)
    columns = (1, 2, 0, 1, 5, 6, 4, 5)

    oldRows = (5,2,5,2)
    oldCols = (1,0,5,4)

    newRows = (4,3,4,3)
    newCols = (2,1,6,5)

    for i in range(0,8):

        clickedNode = (rows[i], columns[i])
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

    # while True:
    #     update_display(WIN, grid,ROWS,WIDTH)

    assert grid[rows[1]][columns[1]].piece.team == 'W'
    assert grid[rows[3]][columns[3]].piece.team == 'R'
    assert grid[rows[5]][columns[5]].piece.team == 'W'
    assert grid[rows[7]][columns[7]].piece.team == 'R'

    assert grid[rows[0]][columns[0]].piece == None
    assert grid[rows[2]][columns[2]].piece == None
    assert grid[rows[4]][columns[4]].piece == None
    assert grid[rows[6]][columns[6]].piece == None


def customCheckerboard():
    width = 800
    rows = 8
    grid = []
    gap = width// rows
    count = 0
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            node = Node(j,i, gap)
            if abs(i-j) % 2 == 0:
                node.colour=BLACK
            if (i == 3 and j == 3):
                node.piece = Man('R')
            if (i == 1 and j == 1):
                node.piece = Man('R')
            if( i == 4 and j == 4):
                node.piece = Man('W')
            if( i == 2 and j == 4):
                node.piece = King('W')
            elif( i == 1 and j == 5):
                node.piece = Man('W')
            count+=1
            grid[i].append(node)
    return grid

def testOnePieceDestroyed():
    grid = customCheckerboard()
    currMove = 'W'
    highlightedPiece = None

    rows = (4,2)
    columns = (4,2)

    for i in range(0,2):

        clickedNode = (rows[i], columns[i])
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

    assert grid[3][3].piece == None
    assert grid[4][4].piece == None
    assert grid[2][2].piece.team == 'W'

    # while True:
    #     update_display(WIN, grid,ROWS,WIDTH)

testFirstFourMoves()
testOnePieceDestroyed()