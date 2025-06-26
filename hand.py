class hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        self.cards.append (card)
        
    def total(self):
        value = sum(card["value"] for card in self.cards)
        aces = sum(1 for card in self.cards if card["value}" == 11])
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value    
    
    def draw(self, surface, y, face_down=False, face_down_card=None):
        for index, card in enumerate(self.cards):
            x = 200 + (index * 100)
            image = card["image"] if index > 0 or not face_down else face_down_card
            surface.blit(image, (x, y))