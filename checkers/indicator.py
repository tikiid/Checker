import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK, GREY

# ne peut pas afficher deux fenêtres avec pygame

class TurnIndicator:
    def __init__(self):
        self.width = 500
        self.height = 200
        self.win = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Tour de jeu')
    
    def update(self, current_turn):
        pygame.init()
        self.win.fill(GREY)
        font = pygame.font.Font(None, 36)
        text = font.render(f'Tour de {current_turn}', True, WHITE)
        text_rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.win.blit(text, text_rect)
        pygame.display.flip()