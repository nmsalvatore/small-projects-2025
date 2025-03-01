# PassJenny

A simple yet powerful passphrase generator that creates memorable but secure passwords.

## Features

- Generate random passphrases with customizable length
- Option to exclude capitalization
- Option to exclude numbers
- Customizable separators between words
- Automatic clipboard copying for easy use

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Build executable

You can build a standalone executable using PyInstaller:

1. Install PyInstaller:
   ```
   pip install pyinstaller
   ```

2. Build the executable:
   ```
   pyinstaller --name passjenny --onefile --add-data "word_list.json:." main.py
   ```

   Note: On Windows, use a semicolon instead of a colon:
   ```
   pyinstaller --name passjenny --onefile --add-data "word_list.json;." main.py
   ```

3. Find the executable in the `dist` directory.

## Usage

### Command Line Options

```
usage: passjenny [-h] [--separator [SEPARATOR]] [--num-words NUM_WORDS] [--no-cap] [--no-num]

PassJenny is an easy-to-use and customizable CLI passphrase generator.

options:
  -h, --help            Show this help message and exit
  --separator [SEPARATOR]
                        Set separator character(s)
  --num-words NUM_WORDS
                        Set number of words
  --no-cap              Don't capitalize words
  --no-num              Don't include number
```

### Examples

Generate a default passphrase (3 words, capitalized, with a number and random separator):
```
passjenny
```

Generate a 5-word passphrase with a plus sign separator:
```
passjenny --num-words 5 --separator "+"
```

Generate a passphrase without capitalization:
```
passjenny --no-cap
```

Generate a passphrase without a number:
```
passjenny --no-num
```

To use a dash separator, use equals syntax to avoid command line confusion:
```
passjenny --separator="--"
```

## Development

### Adding Words to the Word List

Edit the `word_list.json` file to add or remove words from the dictionary.

### Custom Formatters

The application uses a custom help formatter to improve the command line interface display. See `cli.py` for implementation details.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
