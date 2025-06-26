import pygame
import random

class Deck:
    def __init__(self):
        self.card_files = [
            f"assets/cards/{suit} {index}.png"
            for suit in ["clubs", "diamonds", "hearts", "spades"]
            for index in range(1, 14)
        ]
        self.cards =[]
        self.load_cards()
        
    def load_cards(self):
        self.cards.clear()
        for file in self.card_files:
            image = pygame.image.load(file).convert_alpha()
            image = pygame.transform.scale(image, (128, 192))
            rank = int(file.split()[1].split('.')[0])
            value = 11 if rank == 1 else 10 if rank >= 11 else rank
            self.cards.append({"image": image, "value": value})