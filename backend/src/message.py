import re

class Message:
    def __init__(self, message=""):
        """
        Initializes a new instance of the Message class with the given message.

        Args:
            message (str): A string representing the message to store.
        """
        self.message = message

    def update_message(self, message: str):
        """
        Updates the stored message to the given string.

        Args:
            message (str): A string representing the new message to store.
        """
        self.message = message

    def remove_spec_char(self):
        """
        Removes all non-alphabetic characters from the stored message.
        """
        self.message = re.sub('[^A-Za-z]+', '', self.message)

    def format_text_to_number(self):
        """
        Formats the stored message into a list of numeric values representing each letter.
        """
        new_message = []
        for l in self.message.upper():
            new_message.append(ord(l) - 64)
        self.message = new_message

    def format_text_list_to_number(self):
        """
        Formats each element in the stored message list into a numeric value representing each letter.
        """
        new_message = []
        self.message = [l.upper() for l in self.message]
        for l in self.message:
            new_message.append(ord(l) - 64)
        self.message = new_message

    def format_number_to_text(self):
        """
        Formats the stored message list of numeric values into a list of letters.
        """
        new_message = []
        for l in self.message:
            new_message.append(chr(l + 64))
        self.message = new_message

    def __len__(self):
        """
        Returns the number of characters in the stored message.
        """
        return len(self.message)

    def obtain_cypher_text(self, keystream: list):
        """
        Applies a Vigenere cipher to the stored message using the given keystream.

        Args:
            keystream (list): A list of numeric values representing the keystream to use.

        Returns:
            result (list): A list of numeric values representing the encrypted message.
        """
        result = []
        for (k,m) in zip(keystream, self.message):
            value = k + m
            if(value > 26):
                result.append(value - 26)
            else:
                result.append(value)

        self.message = result

    def decrypt_message(self, keystream: list):
        """
        Decrypts the stored message using a Vigenere cipher and the given keystream.

        Args:
            keystream (list): A list of numeric values representing the keystream to use.

        Returns:
            result (list): A list of numeric values representing the decrypted message.
        """
        result = []
        for (c,k) in zip(self.message, keystream):
            if c < k:
                result.append(c + 26 - k)
            else:
                result.append(c - k)

        self.message = result
