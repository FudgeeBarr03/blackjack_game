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