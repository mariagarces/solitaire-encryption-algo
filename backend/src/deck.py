import random
from .card import Card

class Deck:
    """
    A class representing a deck of playing cards.
    
    """
    def __init__(self, cards=[]):
        """
        Initializes a new deck with the given cards, or builds a new deck if no cards are provided.

        Args:
            cards (list): A list of Card objects representing the cards in the deck.
        """
        self.cards = cards
        if cards == []:
            self.build()

    def update_deck(self, first: list, middle: list, last: list):
        """
        Updates the deck with the given lists of cards.

        Args:
            first (list): A list of Card objects representing the cards to be placed at the beginning of the deck.
            middle (list): A list of Card objects representing the cards to be placed in the middle of the deck.
            last (list): A list of Card objects representing the cards to be placed at the end of the deck.
        """
        self.cards = []
        self.cards = first + middle + last

    def build(self):
        """
        Builds a new deck of 52 cards plus 2 jokers.
        """
        self.cards = []
        # Club->Trèfle , Diamond->Carreau , Heart->Coeur, Spade->Pique
        for s in ["C", "D", "H", "S"]:
            for v in range(1,14):
                self.cards.append(Card(s, v))

        self.cards.append(Card("BJ", 53))
        self.cards.append(Card("RJ", 53))

    def shuffle(self):
        """
        Shuffles the cards in the deck.
        """
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        """
        Prints the cards in the deck.
        """
        for c in self.cards:
            c.show()

    def get_joker_index(self, suit: str):
        """
        Returns the index of the joker card with the given suit, or None if it's not in the deck.

        Args:
            suit (str): A string representing the suit of the joker card to find.

        Returns:
            index (int): An integer representing the index of the joker card with the given suit, or None if it's not in the deck.
        """
        for index, c in enumerate(self.cards):
            if c.suit == suit:
                return index
        return None

    def remove_joker_card(self, suit: str):
        """
        Removes the joker card with the given suit from the deck.

        Args:
            suit (str): A string representing the suit of the joker card to remove.
        """
        for index, c in enumerate(self.cards):
            if c.suit == suit:
                self.cards.pop(index)

    def __len__(self):
        """
        Returns the number of cards in the deck.
        """
        return len(self.cards)

    def __getitem__(self, value: int):
        """
        Returns the card at the given index in the deck.

        Args:
            value (int): An integer representing the index of the card to return.

        Returns:
            card (Card): A Card object representing the card at the given index in the deck.
        """
        return self.cards[value]
