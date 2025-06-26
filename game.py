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
            
            if self.player_in and not self.game_over:
                if self.hit_button.draw(self.screen):
                    self.deck.deal_card(self.player)
                    if self.player.total() >= 21:
                        self.player_in = False
                        self.game_over = True
                        
            if not self.player_in and self.dealer_in:
                while self.dealer.total() < 17:
                    self.deck.deal_card(self.dealer)
                self.dealer_in = False
                self.game_over = True
                