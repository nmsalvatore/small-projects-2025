#!/usr/bin/env python3

import argparse
import json
import random
import os
import pathlib

import dotenv
import pyperclip


dotenv.load_dotenv()


class Passphrase:
    def __init__(self):
        self._separator = os.getenv(
            "CUSTOM_SEPARATOR",
            self._choose_random_separator()
        )
        self.passphrase = self._generate_passphrase()

    def _get_word_list(self) -> list:
        word_list_path = pathlib.Path(__file__).resolve().with_name("word_list.json")
        with open(word_list_path, "r") as file:
            return json.load(file)

    def _choose_random_separator(self) -> str:
        separator_options = ["-", "+", "~", ":"]
        return random.choice(separator_options)

    def _choose_random_words(self) -> list:
        words = []
        for _ in range(3):
            word = random.choice(self._get_word_list()).capitalize()
            words.append(word)
        return words

    def _add_num_to_word(self, words: list) -> list:
        random_number = random.randint(0, 9)
        random_index = random.randint(0, len(words) - 1)
        words[random_index] = words[random_index] + str(random_number)
        return words

    def _generate_passphrase(self) -> str:
        words = self._choose_random_words()
        words_with_num = self._add_num_to_word(words)
        return f"{self._separator}".join(words_with_num)

    def __str__(self):
        return self.passphrase


if __name__ == "__main__":
    passphrase = Passphrase()
    pyperclip.copy(passphrase)

    if pyperclip.paste() == str(passphrase):
        print("Password has been copied to clipboard!")
    else:
        print("Password could not be copied to clipboard. Password is:", passphrase)
