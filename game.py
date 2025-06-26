import pygame
from deck import Deck
from hand import Hand
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("BlackJack")
        
    def get_font(self, size):
        return pygame.font.Font(None, size)

    def run(self):
        while self.running:
            self.screen.fill((202, 228, 241))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            pygame.display.update()
        pygame.quit()
