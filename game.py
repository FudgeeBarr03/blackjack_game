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

    def load_buttons(self):
        self.start_button = Button(320, 500, pygame.image.load("assets/buttons/start_btn.png"), 1)
        self.exit_button = Button(670, 500, pygame.image.load("assets/buttons/exit_btn.png"), 1)
        self.hit_button = Button(300, 600, pygame.image.load("assets/buttons/hit.png"),0.6)
        self.stand_button = Button(600, 600, pygame.image.load("assets/buttons/stand.png"), 0.6)
        self.retry_button = Button(220, 250, pygame.image.load("assets/buttons/retry.png"), 0.6)
        self.title_button = Button(300, 120, pygame.image.load("assets/buttons/title.png"), 3)
    
    def run(self):
        while self.running:
            self.screen.fill((202, 228, 241))
            self.title_button.draw(self.screen)
            if self.start_button.draw(self.screen):
                self.play_game()
            elif self.exit_button.draw(self.screen):
                self.running = False
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
            self.deck.deal_card(self.player)
            self.deck.deal_card(self.dealer)
            
        playing = True
        while playing:
            self.screen.fill((0, 128, 0))
            self.dealer.draw(self.screen, 30, face_down=not self.game_over, face_down_card=self.face_down_card)
            self.player.draw(self.screen, 380)
            
            self.screen.blit(self.get_font(45).render(f"Your total: {self.player.total()}", True, "white"), (450, 550))
            
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
                
            if self.game_over:
                self.screen.blit(self.get_font(45).render(f"Dealer's total: {self.dealer.total()}", True, "White"), (450, 200))
                result = self.check_winner()
                self.screen.blit(self.get_font(45).render(result, True, "White"), (450, 280))
                if self.retry_button.draw(self.screen):
                    self.play_game()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                    self.running = False
            pygame.display.update()
    
    def check_winner(self):
        player_score = self.player.total()
        dealer_score = self.dealer.total()
        if player_score >21 or player_score > dealer_score > 21:
            return "Dealer wins!"
        elif dealer_score >21 or player_score > dealer_score or player_score == 21:
            return "You win!"
        elif 21 <= dealer_score > player_score:
            return "Dealer wins!"
        elif dealer_score and player_score > 21:
            return "Its a tie!"
        else:
            return "Its a tie!"