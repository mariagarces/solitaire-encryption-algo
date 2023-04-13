from .card import Card
from .deck import Deck

"""
This module provides a class for encryption using a deck of cards.

The `Encryption` class contains methods for moving cards in the deck, executing
a triple cut, executing a count cut, finding the output value, and executing the
encryption process. 

Example usage:

    deck = Deck()
    encryption = Encryption(deck)
    keystream = encryption.execute_encryption("SECRETMESSAGE")
    print(keystream)
"""
class Encryption:
    def __init__(self, deck: list):
        """
        Initializes an Encryption object with a deck of cards.

        Args:
            deck (list): A list of Card objects representing a deck of cards.
        """
        self.deck = deck

    def move_positions(self, pos: int, dis: int, joker: Card):
        """
        Moves cards in the deck based on the specified position, distance, and joker card.

        Args:
            pos (int): An integer representing the starting position in the deck.
            dis (int): An integer representing the distance to move from the starting position.
            joker (Card): A Card object representing the joker card to be moved.
        """
        self.deck.remove_joker_card(joker.suit)
        step = pos + dis
        left_deck = self.deck[:step]
        right_deck = self.deck[step:]

        if len(self.deck) == pos:
            self.deck.update_deck(left_deck[:dis], [joker],  left_deck[dis:])
        elif len(self.deck)-1 == pos and joker.suit == "RJ":
            self.deck.update_deck(left_deck[:1], [joker], left_deck[1:])
        else:
            self.deck.update_deck(left_deck, [joker], right_deck)

    def move_black_joker(self):
        """
        Moves the black joker card in the deck.
        """
        index = self.deck.get_joker_index("BJ")
        self.move_positions(index, 1, Card("BJ", 53))

    def move_red_joker(self):
        """
        Moves the red joker card in the deck.
        """
        index = self.deck.get_joker_index("RJ")
        self.move_positions(index, 2, Card("RJ", 53))

    def execute_triple_cut(self):
        """
        Executes a triple cut in the deck.
        """
        black_joker_index = self.deck.get_joker_index("BJ")
        red_joker_index = self.deck.get_joker_index("RJ")

        if black_joker_index > red_joker_index:
            deck_after_black_joker = self.deck[black_joker_index+1:]
            deck_before_red_joker = self.deck[:red_joker_index]
            middle_deck = self.deck[red_joker_index:black_joker_index+1]
            self.deck.update_deck(deck_after_black_joker, middle_deck, deck_before_red_joker)
        else:
            deck_before_black_joker = self.deck[:black_joker_index]
            deck_after_red_joker = self.deck[red_joker_index+1:]
            middle_deck = self.deck[black_joker_index:red_joker_index+1]
            self.deck.update_deck(deck_after_red_joker, middle_deck, deck_before_black_joker)

    def execute_count_cut(self):
        """
        Executes a count cut in the deck.
        """
        bottom_card = self.deck[-1].get_real_value()
        cut_deck = self.deck[:bottom_card]
        middle_deck = self.deck[bottom_card:len(self.deck)-1]
        final_card = self.deck[-1]
        self.deck.update_deck(middle_deck, cut_deck, [final_card])

    def find_output_value(self) -> int:
        """
        Finds the output value of the deck.

        Returns:
            An integer representing the output value of the deck.
        """
        index = self.deck[0].get_real_value()
        if index == "RJ":
            value = index
        else:
            value = self.deck[index].get_real_value()

        if value == 53:
            return -1

        if value > 26 :
            return value - 26

        return value

    def execute_encryption(self, message: str) -> list:
        """
        Executes the encryption process using the deck and a message.

        Args:
            message (str): A string representing the message to be encrypted.

        Returns:
            A list of integers representing the keystream values.
        """
        l = 0
        keystream = []

        while l < len(message):
            self.move_black_joker()
            self.move_red_joker()
            self.execute_triple_cut()
            self.execute_count_cut()
            output_value = self.find_output_value()

            if output_value != -1:
                keystream.append(output_value)
                l += 1

        return keystream