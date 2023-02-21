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

def test_remove_one_joker(deck):
    deck.remove_joker_card("BJ")
    assert len(deck.cards) == 53
