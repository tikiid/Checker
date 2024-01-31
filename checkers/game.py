import pygame
from .constants import BLACK, WHITE, SQUARE_SIZE, HEIGHT, WIDTH, BLUE
from .board import Board


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    # rafraîchir l'affichage
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        self.display_current_turn()
        pygame.display.update()

    # default settings (private)
    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = WHITE
        self.valid_moves = {}

    # affiche la couleur qui doit jouer
    def display_current_turn(self):
            display_text = f"Turn: {self.get_turn_color()}"
            font = pygame.font.SysFont('arial', 24)
            turn_text = font.render(display_text, True, WHITE)
            text_width, text_height = font.size(display_text)
            self.win.blit(turn_text, (WIDTH // 2 - text_width, HEIGHT - 30))

    def get_turn_color(self):
        return "White" if self.turn == WHITE else "Black"

    def reset(self):
        self._init()

    def winner(self):
        return self.board.winner()

    # sélectionner une pièce 
    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            # reset sélection  
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
        # check si coup possible au clic de la souris
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            # tuer
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else: 
            return False
        
        return True

    # afficher les mouvements possibles d'une pièce    
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

