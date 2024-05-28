import re

class MyString:

    def __init__(self, value=""):
        """
        Initializes the MyString class with a value.
        If the value provided is not a string, it sets an empty string as the value.
        """
        if not isinstance(value, str):
            print("The value must be a string.")
            self._value = ""
        else:
            self._value = value

    @property
    def value(self):
        """Getter method to retrieve the value."""
        return self._value

    @value.setter
    def value(self, val):
        """
        Setter method to modify the value.
        If the provided value is not a string, it displays an error message.
        """
        if not isinstance(val, str):
            print("The value must be a string.")
        else:
            self._value = val

    def is_sentence(self):
        """Checks if the value ends with a period."""
        return self.value.endswith(".")

    def is_question(self):
        """Checks if the value ends with a question mark."""
        return self.value.endswith("?")

    def is_exclamation(self):
        """Checks if the value ends with an exclamation mark."""
        return self.value.endswith("!")

    def count_sentences(self):
        """
        Determines the count of sentences in the value.
        Splits the string based on periods, question marks, and exclamation marks and returns the count.
        """
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)

# Example usage:
my_string = MyString("Hello! How are you? I am fine.")
print(my_string.count_sentences())  # Output: 3
