import pygame
pygame.init()
from checkers.properties import *
from checkers.checkerboard import *
import sys



def main(WIDTH, ROWS):
    grid = make_grid(ROWS, WIDTH)
    highlightedPiece = None
    currMove = 'W'
    info = font.render("Aby zresetować grę naciśnij dowolny przycisk na klawiaturze.", True, RED)
    WIN.blit (info, (50, 830))
    


    while True:

        if currMove == 'W':
            WIN.blit (WHITETURN, (50, 870))
        elif currMove == 'R':
            WIN.blit (REDTURN, (50, 870))


        if showWinner() == 'R':
            WIN.blit (REDWIN, (50, 870))
            grid = make_grid(ROWS, WIDTH)
        elif showWinner() == 'W':
            WIN.blit (WHITEWIN, (50, 870))
            grid = make_grid(ROWS, WIDTH)
        

        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                print('EXIT SUCCESSFUL')
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                resetPieces()
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