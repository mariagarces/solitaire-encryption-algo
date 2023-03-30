from src.deck import Deck
from src.card import Card
import pytest

@pytest.fixture
def deck():
    return Deck()

def test_build(deck):
    assert len(deck.cards) == 54

def test_get_index_black_joker(deck):
    assert deck.get_joker_index("BJ") == 52

def test_get_index_red_joker(deck):
    assert deck.get_joker_index("RJ") == 53

def test_update_deck(deck):
    first = deck[:26]
    last = deck[26:-2]
    middle = deck[52:54]
    deck.update_deck(first, middle, last)
    assert deck[0].value == 1 and deck[0].suit == "C"
    assert deck[-1].value == 13 and deck[-1].suit == "S"

def test_remove_one_joker(deck):
    deck.remove_joker_card("BJ")
    assert len(deck.cards) == 53
