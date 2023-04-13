from .deck import *
from .encryption import *
from .message import *

"""
This module provides the Main class, which is the main entry point for using the Solitaire Cipher algorithm.

The Solitaire Cipher is a symmetric encryption algorithm that uses a deck of playing cards to generate a keystream,
which is then used to encrypt and decrypt messages. This implementation is based on Bruce Schneier's design.
"""
class Main:
    def __init__(self):
        """
        Initializes a new instance of the Main class, creating a deck of cards and a message object.
        """
        self.deck = Deck()
        self.message = Message()
        keystream = []

    def load_message(self, message: str):
        """
        Loads the specified message into the message object, removing special characters and formatting it for encryption.
        
        Args:
            message: A string containing the message to be encrypted or decrypted.
        """
        self.message.update_message(message)
        self.message.remove_spec_char()
        self.message.format_text_to_number()

    def get_key_cards(self) -> Deck:
        """
        Returns the deck of cards in its initial order.

        Returns:
            A Deck object representing the deck of cards in its initial order.
        """
        self.deck.build()
        return self.deck

    def get_key_cards_shuffle(self) -> Deck:
        """
        Returns the deck of cards in a shuffled order.
  
        Returns:
            A Deck object representing the deck of cards in a shuffled order.
        """
        self.deck.shuffle()
        return self.deck

    def get_current_state_cards(self) -> Deck:
        """
        Returns the current state of the deck of cards.
  
        Returns:
            A Deck object representing the current state of the deck of cards.
        """
        return self.deck

    def get_encrypted_message(self) -> Message:
        """
        Encrypts the message using the current deck of cards, returning a new message object with the encrypted text.
  
        Returns:
            A Message object representing the encrypted message.
        """
        encryption = Encryption(self.deck)
        self.keystream = encryption.execute_encryption(self.message)
        self.message.obtain_cypher_text(self.keystream)
        self.message.format_number_to_text()
        return self.message

    def get_decrypted_message(self) -> Message:
        """
        Decrypts the message using the current deck of cards, returning a new message object with the decrypted text.
        
        Returns:
            A Message object representing the decrypted message.
        """
        self.message.format_text_list_to_number()
        self.message.decrypt_message(self.keystream)
        self.message.format_number_to_text()
        return self.message

    def load_cards(self, cards: list):
        """
        Loads a list of card dictionaries into the deck object.

        Args:
            cards: A list of dictionaries representing the cards to be loaded into the deck.
        """
        cards_data = []
        for c in cards:
            cards_data.append(Card(**c))

        deck = Deck(cards_data)
        self.deck = deck