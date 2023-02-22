from .deck import *
from .encryption import *
from .message import *

# deck = Deck()
# deck.shuffle()
# deck.show()

# encryption = Encryption(deck)
# encryption.move_black_joker()
# encryption.move_red_joker()
# encryption.execute_triple_cut()
# encryption.execute_count_cut()
# value = encryption.find_output_value()
# print(value)
# deck.show()

# value = encryption.execute_encryption(new_message)

# print(value)


class Main:
    def __init__(self):
        self.deck = Deck()
        self.message = Message()

    def load_message(self, message):
        self.message.update_message(message)
        self.message.remove_spec_char()
        self.message.format_text_to_number()

    def get_key_cards(self):
        self.deck.build()
        return self.deck

    def get_key_cards_shuffle(self):
        self.deck.shuffle()
        return self.deck

    def get_encrypted_message(self):
        encryption = Encryption(self.deck)
        keystream = encryption.execute_encryption(self.message)
        self.message.obtain_cypher_text(keystream)
        self.message.format_number_to_text()
        return self.message