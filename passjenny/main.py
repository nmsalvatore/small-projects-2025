#!/usr/bin/env python3

import argparse
import textwrap

import pyperclip

from passjenny.cli import PassJennyArgumentParser
from passjenny.passphrase import Passphrase


if __name__ == "__main__":
    parser = PassJennyArgumentParser()
    args = parser.parse_args()

    passphrase = Passphrase(
        capitalize=args.capitalize,
        include_num=args.include_num,
        separator=args.separator,
        num_words=args.num_words,
    )

    pyperclip.copy(passphrase)

    if pyperclip.paste() == str(passphrase):
        print("Your new passphrase has been copied to the clipboard!")
    else:
        message = f"""\
            Passphrase could not be copied to clipboard.
            Your new passphrase is: {passphrase}"""
        print(textwrap.dedent(message))
