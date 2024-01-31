import pygame

# Variables du board
WIDTH, HEIGHT = 800, 830
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# couleurs
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE =  (0, 0, 255)
GREY =  (85, 85, 85)
GREEN = (0,255,0)

# Dame noir et blanc
BLACK_QUEEN = pygame.image.load("assets/black_queen.png")
WHITE_QUEEN = pygame.image.load("assets/white_queen.png")
# Pion noir et blanc
BLACK_PAWN = pygame.image.load("assets/black_pawn.png")
WHITE_PAWN = pygame.image.load("assets/white_pawn.png")