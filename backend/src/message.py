import re

class Message:
    def __init__(self, message=""):
        self.message = message

    def update_message(self, message: str):
        self.message = message

    def remove_spec_char(self):
        self.message = re.sub('[^A-Za-z]+', '', self.message)

    def format_text_to_number(self):
        new_message = []
        for l in self.message.upper():
            new_message.append(ord(l) - 64)
        self.message = new_message

    def format_text_list_to_number(self):
        new_message = []
        self.message = [l.upper() for l in self.message]
        for l in self.message:
            new_message.append(ord(l) - 64)
        self.message = new_message

    def format_number_to_text(self):
        new_message = []
        for l in self.message:
            new_message.append(chr(l + 64))
        self.message = new_message

    def __len__(self):
        return len(self.message)

    def obtain_cypher_text(self, keystream: list):
        result = []
        for (k,m) in zip(keystream, self.message):
            value = k + m
            if(value > 26):
                result.append(value - 26)
            else:
                result.append(value)

        self.message = result

    def decrypt_message(self, keystream: list):
        result = []
        for (c,k) in zip(self.message, keystream):
            if c < k:
                result.append(c + 26 - k)
            else:
                result.append(c - k)

        self.message = result
