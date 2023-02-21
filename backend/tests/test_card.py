from src.card import Card

def test_get_real_value_clubs_card():
    card = Card("C", 3)
    assert card.get_real_value() == 3

def test_get_real_value_diamonds_card():
    card = Card("D", 7)
    assert card.get_real_value() == 20

def test_get_real_value_hearts_card():
    card = Card("H", 2)
    assert card.get_real_value() == 28

def test_get_real_value_spades_card():
    card = Card("S", 5)
    assert card.get_real_value() == 44

def test_get_real_value_jokers():
    card = Card("RJ", 53)
    assert card.get_real_value() == 53
