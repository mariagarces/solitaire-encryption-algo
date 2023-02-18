from card import *
from deck import *

class Encryption:
    def __init__(self, deck):
        self.deck = deck
        #encrypted message?

    def move_positions(self, pos, dis, joker):
        self.deck.remove_card(joker.suit)
        step = pos + dis
        left_deck = self.deck[:step]
        right_deck = self.deck[step:]

        if len(self.deck) == pos:
            # when jocker is last
            self.deck.update_deck(left_deck[:dis], [joker],  left_deck[dis:])
        elif len(self.deck)-1 == pos and joker.suit == "RJ":
            self.deck.update_deck(left_deck[:1], [joker], left_deck[1:])
        else:
            # when joker is in the middle
            self.deck.update_deck(left_deck, [joker], right_deck)

    def move_black_joker(self):
        index = self.deck.get_index("BJ")
        self.move_positions(index, 1, Card("BJ", 53))

    def move_red_joker(self):
        index = self.deck.get_index("RJ")
        self.move_positions(index, 2, Card("RJ", 53))

    def execute_triple_cut(self):
        black_joker_index = self.deck.get_index("BJ")
        red_joker_index = self.deck.get_index("RJ")

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
        bottom_card = self.deck[-1].get_real_value()
        cut_deck = self.deck[:bottom_card]
        middle_deck = self.deck[bottom_card:len(self.deck)-1]
        final_card = self.deck[-1]
        self.deck.update_deck(middle_deck, cut_deck, [final_card])

    def find_output_value(self):
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

    def execute_encryption(self, message):
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