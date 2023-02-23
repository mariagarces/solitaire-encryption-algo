from .deck import *
from .encryption import *
from .message import *

class Main:
    def __init__(self):
        self.deck = Deck()
        self.message = Message()
        keystream = []

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

    def get_current_state_cards(self) -> Deck:
        return self.deck

    def get_encrypted_message(self) -> Message:
        encryption = Encryption(self.deck)
        self.keystream = encryption.execute_encryption(self.message)
        self.message.obtain_cypher_text(self.keystream)
        self.message.format_number_to_text()
        return self.message

    def get_decrypted_message(self) -> Message:
        self.message.format_text_list_to_number()
        self.message.decrypt_message(self.keystream)
        self.message.format_number_to_text()
        return self.message

    def load_cards(self, cards: list):
        cards_data = []
        for c in cards:
            cards_data.append(Card(**c))

        deck = Deck(cards_data)
        self.deck = deck