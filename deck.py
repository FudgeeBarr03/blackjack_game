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
        
    