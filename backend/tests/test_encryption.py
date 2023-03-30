from src.encryption import Encryption
from src.card import Card
from src.deck import Deck
import pytest

def compare_lists(list1, list2):
    for (card1, card2) in zip(list1, list2):
        if card1.suit != card2.suit or card1.value != card2.value:
            return False
    return True

@pytest.fixture
def encrypt():
    deck = Deck([Card('C',1),Card('H',2),Card('H',3),Card('H',4),Card("BJ", 53),Card("RJ", 53)])
    return Encryption(deck)

def test_move_positions(encrypt):
    encrypt.move_positions(4,1,Card("BJ", 53))
    deck = [Card('C',1),Card('H',2),Card('H',3),Card('H',4),Card("RJ", 53),Card("BJ", 53)]
    assert compare_lists(encrypt.deck, deck) == True

def test_move_black_joker(encrypt):
    encrypt.move_black_joker()
    deck = [Card('C',1),Card('H',2),Card('H',3),Card('H',4),Card("RJ", 53),Card("BJ", 53)]
    assert compare_lists(encrypt.deck, deck) == True

def test_move_black_joker_last_position(encrypt):
    encrypt.move_black_joker()
    encrypt.move_black_joker()
    deck = [Card('C',1),Card("BJ", 53),Card('H',2),Card('H',3),Card('H',4),Card("RJ", 53)]
    assert compare_lists(encrypt.deck, deck) == True

def test_move_red_joker_last_position(encrypt):
    encrypt.move_red_joker()
    deck = [Card('C',1),Card('H',2),Card("RJ", 53),Card('H',3),Card('H',4),Card("BJ", 53)]
    assert compare_lists(encrypt.deck, deck) == True

def test_move_red_joker_before_last_position(encrypt):
    for _ in range(3):
        encrypt.move_red_joker()
    
    deck = [Card('C',1),Card("RJ", 53),Card('H',2),Card('H',3),Card('H',4),Card("BJ", 53)]
    assert compare_lists(encrypt.deck, deck) == True

def test_execute_triple_cut(encrypt):
    encrypt.execute_triple_cut()
    deck = Deck([Card("BJ", 53),Card("RJ", 53),Card('C',1),Card('H',2),Card('H',3),Card('H',4)])
    assert compare_lists(encrypt.deck, deck) == True

def test_execute_triple_cut_bj_after(encrypt):
    encrypt.move_black_joker()
    encrypt.execute_triple_cut()
    deck = Deck([Card("RJ", 53),Card("BJ", 53),Card('C',1),Card('H',2),Card('H',3),Card('H',4)])
    assert compare_lists(encrypt.deck, deck) == True

def test_execute_count_cut(encrypt):
    encrypt.execute_triple_cut()
    encrypt.execute_count_cut()
    deck = Deck([Card("BJ", 53),Card("RJ", 53),Card('C',1),Card('H',2),Card('H',3),Card('H',4)])
    assert compare_lists(encrypt.deck, deck) == True

def test_find_output_value(encrypt):
    value = encrypt.find_output_value()
    assert value == 2