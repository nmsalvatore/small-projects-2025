import json
import random

from pathlib import Path


class Passphrase:
    def __init__(self, capitalize=True, include_num=True, separator=None, num_words=3):
        self._capitalize = capitalize
        self._include_num = include_num
        self._separator = separator
        self._num_words = num_words
        self._passphrase = self._generate_passphrase()

    def _get_word_list(self) -> list:
        word_list_path = Path(__file__).resolve().with_name("word_list.json")
        with open(word_list_path, "r") as file:
            return json.load(file)

    def _choose_random_separator(self) -> str:
        separator_options = ["-", "+", "~"]
        return random.choice(separator_options)

    def _choose_random_words(self) -> list:
        words = []
        for _ in range(self._num_words):
            word = random.choice(self._get_word_list())
            words.append(word.capitalize() if self._capitalize else word)
        return words

    def _add_num_to_word(self, words: list) -> list:
        random_number = random.randint(0, 9)
        random_index = random.randint(0, len(words) - 1)
        words[random_index] = words[random_index] + str(random_number)
        return words

    def _generate_passphrase(self) -> str:
        words = self._choose_random_words()
        separator = self._separator or self._choose_random_separator()
        words = self._add_num_to_word(words) if self._include_num else words
        return f"{separator}".join(words)

    def __str__(self):
        return self._passphrase
