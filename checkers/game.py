import pygame
from .constants import BLACK, WHITE, BLUE, SQUARE_SIZE
from checkers.board import Board
from checkers.indicator import TurnIndicator


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # rafraîchir l'affichage
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()


    # default settings (private)
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}


    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()


    # sélectionner une pièce 
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            # reset selection recall 
            if not result: 
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece 
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
        
        return False

    # bouger une piece
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else: 
            return False
        
        return True

    # afficher les mouvements d'une pièce    
    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, WHITE, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 10) 
            pygame.draw.circle(self.win, BLACK, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 5) 

    # changer le tour
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == WHITE:
            self.turn = BLACK
        else:
            self.turn = WHITE

