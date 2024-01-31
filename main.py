import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, ROWS, COLS
from checkers.board import Board
from checkers.game import Game
from checkers.indicator import TurnIndicator

FPS = 60 

WIN = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('Checkers')


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def main():
    run = True

    # pour l'affichage de la font
    pygame.init()
    # pour les FPS de la fenêtre
    clock = pygame.time.Clock() 
    game = Game(WIN)

    while run: 
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT: # quitter la page
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # make sure user is clicking on the board 
                if 0 <= row < ROWS and 0 <= col < COLS:
                    game.select(row, col)

            if event.type == pygame.KEYDOWN:
                # reset the game
                if event.key == pygame.K_r:
                    game.reset()
                
                # quit the game
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

        game.update()

    pygame.quit()

main()
