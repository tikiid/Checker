import pygame
from .constants import BLACK, ROWS, COLS, WHITE, RED, SQUARE_SIZE
from .pieces import Piece

# Create class board
class Board:
    def __init__(self):
        self.board = []
        self.black_left = self.white_left = 12
        self.black_queen = self.white_queen = 0
        self.create_board()

    # Dessiner le BOARD (background noir, ajout des cases blanches)
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range (ROWS):
           for col in range(row % 2, ROWS, 2): 
               pygame.draw.rect(win, WHITE, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    # move -> delete the current piece and draw in another tile
    def move(self, piece, row, col):
        # interchanger les pièces
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)
 
        if row == ROWS - 1 or row == 0:
            piece.make_queen()
            if piece.color == WHITE:
                self.white_queen += 1
            else:
                self.black_queen += 1

    def is_movable(self):
        pass
    
    # prendre la pièce sur le BOARD
    def get_piece(self, row, col):
        return self.board[row][col]

    # Ajout des piecès dans le BOARD
    def create_board(self):
        for row in range (ROWS):
            # nouvelle rangé
            self.board.append([])
            for col in range (COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, BLACK))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, WHITE))
                    else: 
                        self.board[row].append(0)
                else: 
                    self.board[row].append(0)
    
    # Dessiner le BOARD
    def draw(self, win):
        # afficher le BOARD
        self.draw_squares(win)
        # dessiner les pièces 
        for row in range (ROWS):
            for col in range (COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(win)

    def winner(self):
        if self.white_left <= 0:
            return BLACK
        else:
            return WHITE
        
        return None

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == WHITE:
                    self.white_left -= 1
                else:
                    self.black_left -= 1

    def get_valid_moves(self, piece):

        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        # mouvements des pions blancs 
        if piece.color == WHITE:
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color, right))

        # mouvements des pions noirs 
        if piece.color == BLACK:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
        
        # mouvements des dames 
        if piece.queen:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))
            moves.update(self._traverse_left(row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row - 1, max(row-3, -1), -1, piece.color, right))
            
        return moves


    def _traverse_left(self, start, stop, step, color, left_col, skipped=[]):
        moves = {}
        last = []
        for current_row in range(start, stop, step):
            if left_col < 0:
                break
            
            current = self.board[current_row][left_col]
            # case vide
            if current == 0:  
                if skipped and not last:
                    break
                elif skipped:
                    moves[(current_row, left_col)] = last + skipped
                else:
                    moves[(current_row, left_col)] = last
                # double ou triple jump
                if last: 
                    if step == -1:
                        row = max(current_row-3, 0)
                    else:
                        row = min(current_row + current_row, ROWS)

                    moves.update(self._traverse_left(current_row + step, row, step, color, left_col - 1, skipped=last))
                    moves.update(self._traverse_right(current_row + step, row, step, color, left_col + 1, skipped=last))
                break
            # même couleur
            elif current.color == color: 
                break
            # assuming jumping over
            else: 
                last = [current]

                left_col -= 1
        
        return moves
        
    def _traverse_right(self, start, stop, step, color, right_col, skipped=[]):
        moves = {}
        last = []
        for current_row in range(start, stop, step):
            if right_col >= COLS:
                break
            
            current = self.board[current_row][right_col]
            if current == 0:  # empty square
                if skipped and not last:
                    break
                elif skipped:
                    moves[(current_row, right_col)] = last + skipped
                else:
                    moves[(current_row, right_col)] = last

                if last: # double or triple jump
                    if step == -1:
                        row = max(current_row-3, 0)
                    else:
                        row = min(current_row + current_row, ROWS)

                    moves.update(self._traverse_left(current_row + step, row, step, color, right_col - 1, skipped=last))
                    moves.update(self._traverse_right(current_row + step, row, step, color, right_col + 1, skipped=last))
                break

            elif current.color == color: # same color => no moves
                break
            else: # assuming jumping over
                last = [current]

                right_col += 1
        
        return moves    
