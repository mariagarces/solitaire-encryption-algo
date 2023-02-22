from .deck import *
from .encryption import *
from .message import *

class Main:
    def __init__(self):
        self.deck = Deck()
        self.message = Message()

    def load_message(self, message: str):
        self.message.update_message(message)
        self.message.remove_spec_char()
        self.message.format_text_to_number()

    def get_key_cards(self) -> Deck:
        self.deck.build()
        return self.deck

    def get_key_cards_shuffle(self) -> Deck:
        self.deck.shuffle()
        return self.deck

    def get_encrypted_message(self) -> Message:
        encryption = Encryption(self.deck)
        keystream = encryption.execute_encryption(self.message)
        self.message.obtain_cypher_text(keystream)
        self.message.format_number_to_text()
        return self.message