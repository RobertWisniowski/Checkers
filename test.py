import pygame
pygame.init()
from checkers.properties import *
from checkers.checkerboard import *
import sys

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

def customCheckerboard2():
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
            if( i == 4 and j == 4):
                node.piece = Man('W')
            count+=1
            grid[i].append(node)
    return grid

def testFirstFourMoves():

    grid = makeGrid(ROWS, WIDTH)
    currMove = 'W'
    highlightedPiece = None

    rows = (5, 4, 2, 3, 5, 4, 2, 3)
    columns = (1, 2, 0, 1, 5, 6, 4, 5)

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


    assert grid[rows[1]][columns[1]].piece.team == 'W'
    assert grid[rows[3]][columns[3]].piece.team == 'R'
    assert grid[rows[5]][columns[5]].piece.team == 'W'
    assert grid[rows[7]][columns[7]].piece.team == 'R'

    assert grid[rows[0]][columns[0]].piece == None
    assert grid[rows[2]][columns[2]].piece == None
    assert grid[rows[4]][columns[4]].piece == None
    assert grid[rows[6]][columns[6]].piece == None

    print('Test nr 1: \"Wykonanie po dwa ruchy przez ka??dego z graczy\" dzia??a.')

def testPieceWrongMove():
    grid = makeGrid(ROWS, WIDTH)
    currMove = 'W'
    highlightedPiece = None

    rows = (5, 4)
    columns = (1, 1)

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

    assert grid[5][1].piece.team == 'W'
    assert grid[4][1].piece == None

    print('Test nr 2: \"Niepowodzenie b????dnego ruchu pionkiem\" dzia??a.')

def testOnePieceDestroyed():
    grid = makeGrid(ROWS, WIDTH)
    currMove = 'W'
    highlightedPiece = None

    rows = (5, 4, 2, 3, 4, 2)
    columns = (1, 2, 0, 1, 2, 0)

    for i in range(0,6):

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

    assert grid[3][1].piece == None
    assert grid[5][1].piece == None
    assert grid[4][2].piece == None
    assert grid[2][0].piece.team == 'W'

    print('Test nr 3: \"Wykonanie bicia pojedynczego pionka\" dzia??a.')

def testTwoPiecesDestroyed():
    grid = customCheckerboard()
    currMove = 'W'
    highlightedPiece = None

    rows = (4, 2, 2, 0)
    columns = (4, 2, 2, 0)

    for i in range(0,4):

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
    assert grid[1][1].piece == None
    assert grid[0][0].piece.team == 'W'

    print('Test nr 4: \"Wykonanie bicia przynajmniej dw??ch pionk??w\" dzia??a.')

def testMakeKing():
    grid = customCheckerboard()
    currMove = 'W'
    highlightedPiece = None

    rows = (1, 0)
    columns = (5, 6)

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

    assert grid[1][5].piece == None
    assert grid[0][6].piece.team == 'W'
    assert grid[0][6].piece.type == 'KING'

    print('Test nr 5: \"Zamiana pionka w damk??\" dzia??a.')

def testPieceDestroyedByKing():
    grid = customCheckerboard()
    currMove = 'W'
    highlightedPiece = None

    rows = (2, 4)
    columns = (4, 2)

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
    assert grid[2][4].piece == None
    assert grid[4][2].piece.team == 'W'
    assert grid[4][2].piece.type == 'KING'

    print('Test nr 6: \"Bicie damk??\" dzia??a.')


def testRedWins():
    grid = customCheckerboard2()
    changePiecesCount(1, 1)
    currMove = 'R'
    highlightedPiece = None

    rows = (3, 5)
    columns = (3, 5)

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

    assert showWinner() == 'R'
    assert showIfGameIsOver() == True

    print('Test nr 7: \"Wygrana gracza graj??cego czerwonymi pionkami\" dzia??a.')

def testRestartGameAfterWin():
    grid = customCheckerboard2()
    changePiecesCount(1, 1)
    currMove = 'R'
    highlightedPiece = None

    rows = (3, 5)
    columns = (3, 5)

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

        if i == 1:
            resetPieces()
            grid = customCheckerboard2()
            highlightedPiece = None
            currMove = 'W'
            WIN.blit (WHITETURN, (50, 870))

    assert showWinner() == 'None'
    assert showIfGameIsOver() == False
    assert grid[3][3].piece.team == 'R'
    assert grid[4][4].piece.team == 'W'

    print('Test nr 8: \"Rozpocz??cie nowej gry po zwyci??stwie jednego z graczy\" dzia??a.')

def main():
    while True:
        print('\nZestaw test??w do projektu p.t. \"Warcaby\".\n\n')
        print('Podaj numer testu:\n')
        print('1: Wykonanie po dwa ruchy przez ka??dego z graczy.\n')
        print('2: Niepowodzenie b????dnego ruchu pionkiem.\n')
        print('3: Wykonanie bicia pojedynczego pionka.\n')
        print('4: Wykonanie bicia przynajmniej dw??ch pionk??w.\n')
        print('5: Zamiana pionka w damk??.\n')
        print('6: Bicie damk??.\n')
        print('7: Wygrana gracza graj??cego czerwonymi pionkami.\n')
        print('8: Rozpocz??cie nowej gry po zwyci??stwie jednego z graczy.\n')

        a = input()
        a = int(a)
        if a == 1:
            testFirstFourMoves()
        elif a == 2:
            testPieceWrongMove()
        elif a == 3:
            testOnePieceDestroyed()
        elif a == 4:
            testTwoPiecesDestroyed()
        elif a == 5:
            testMakeKing()
        elif a == 6:
            testPieceDestroyedByKing()
        elif a == 7:
            testRedWins()
        elif a == 8:
            testRestartGameAfterWin()
        else:
            print('Nie ma takiej warto??ci na li??cie')

main()