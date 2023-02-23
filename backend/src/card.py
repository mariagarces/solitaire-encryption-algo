import json

class Card:
    def __init__(self, suit: str, value: int):
        self.suit = suit
        self.value = value

    def get_real_value(self) -> int:
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
        print("{} {}".format(self.value, self.suit))

    def from_json(cls, json_string):
        json_dict = json.loads(json_string)
        return cls(**json_dict)
