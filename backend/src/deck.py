import random
from .card import Card

class Deck:
    def __init__(self, cards=[]):
        self.cards = cards
        if cards == []:
            self.build()

    def update_deck(self, first, middle, last):
        self.cards = []
        self.cards = first + middle + last

    def build(self):
        self.cards = []
        for s in ["C", "D", "H", "S"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))

        self.cards.append(Card("BJ", 53))
        self.cards.append(Card("RJ", 53))

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def get_joker_index(self, suit):
        for index, c in enumerate(self.cards):
            if c.suit == suit:
                return index
        return None

    def remove_joker_card(self, suit):
        for index, c in enumerate(self.cards):
            if c.suit == suit:
                self.cards.pop(index)

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, value):
        return self.cards[value]
