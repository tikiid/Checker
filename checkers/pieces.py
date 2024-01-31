import pygame
from .constants import WHITE, BLACK, GREY, GREEN, SQUARE_SIZE, BLACK_PAWN, BLACK_QUEEN, WHITE_PAWN, WHITE_QUEEN

class Piece: 

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.queen = False
        self.selectable = False
        self.x_pos = 0
        self.y_pos = 0
        self.calc_pos()
    
    def calc_pos(self):
        self.x_pos = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y_pos = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_queen(self):
        self.queen = True

    def draw_piece(self, win):
        # affichage des images pour les dames
        if self.queen:
            if self.color == WHITE: 
                win.blit(WHITE_QUEEN, (self.x_pos - WHITE_QUEEN.get_width()//2, self.y_pos - WHITE_QUEEN.get_height()//2))
            elif self.color == BLACK: 
                win.blit(BLACK_QUEEN, (self.x_pos - BLACK_QUEEN.get_width()//2, self.y_pos - BLACK_QUEEN.get_height()//2))
        # affichage des images pour les pions
        else:
            if self.color == BLACK: 
                 win.blit(BLACK_PAWN, (self.x_pos - BLACK_PAWN.get_width()//2, self.y_pos - BLACK_PAWN.get_height()//2))
            elif self.color == WHITE:
                win.blit(WHITE_PAWN, (self.x_pos - WHITE_PAWN.get_width()//2, self.y_pos - WHITE_PAWN.get_height()//2))

    def is_selected(self):
        return self.selected
    
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()
    