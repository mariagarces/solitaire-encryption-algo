import json

class Card:
    """
    A class representing a playing card.

    """
    def __init__(self, suit: str, value: int):
        """
        Initializes a new Card object with the given suit and value.

        Args:
            suit (str): The suit of the card, represented by a single letter ("C", "D", "H", or "S").
            value (int): The face value of the card, ranging from 1 to 13.
        """
        self.suit = suit
        self.value = value

    def get_real_value(self) -> int:
        """
        Returns the real value of the card according to its suit.

        Returns:
            int: The real value of the card.
        """
        if self.suit == "C":
            return self.value
        elif self.suit == "D":
            return self.value + 13
        elif self.suit == "H":
            return self.value + 26
        elif self.suit == "S":
            return self.value + 39
        else:
            return 53

    def show(self):
        """
        Prints the value and suit of the card.
        """
        print("{} {}".format(self.value, self.suit))

    def from_json(cls, json_string):
        """
        Returns a new Card object from a JSON string.

        Args:
            json_string (str): A JSON string representing a Card object.

        Returns:
            Card: A new Card object created from the JSON string.
        """
        json_dict = json.loads(json_string)
        return cls(**json_dict)
