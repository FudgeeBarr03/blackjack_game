import pygame
from deck import Deck
from hand import Hand
from button import Button

class Game:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.screen_width, self.screen_height = 1280, 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("BlackJack")
        
        self.deck = Deck()
        self.player = Hand()
        self.dealer = Hand()
        
        self.running = True
        self.game_over = False
        self.player_in = True
        self.dealer_in = True
        
        self.face_down_card = pygame.transform.scale(pygame.image.load("assets/cards/card back 3.png").convert_alpha(), (128, 192))
        
        self.load_buttons()
        
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

    def play_game(self):
        self.player = Hand()
        self.dealer = Hand()
        self.player_in = True
        self.dealer_in = True
        self.game_over = False
        
        for _ in range(2):
            self.deck.deal_card(self.plaeyer)
            self.deck.deal_card(self.dealer)
            
        playing = True
        while playing:
            self.screen.fill((0, 128, 0))
            self.dealer.draw(self.screen, 30, face_down=not self.game_over, face_down_card=self.face_down_card)
            self.player.draw(self.screen, 380)
            
            self.screen.blit(self.get_font(45).render)(f"Your total: {self.player.total()}", True, "white"), (450, 550)