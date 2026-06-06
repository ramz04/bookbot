# bookbot

A command-line tool that analyzes the word and character frequency of any plain-text book.

## Prerequisites

- **Python 3.14+**
- **uv** – fast Python package manager

Install `uv` (if you don't have it):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on Windows (PowerShell):

```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

## Installation

```bash
git clone https://github.com/your-username/bookbot.git
cd bookbot
uv sync
```

## Usage

```bash
python3 main.py <path_to_book>
```

### Example

```bash
python3 main.py books/frankenstein.txt
```

Sample output:

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 75767 total words
--------- Character Count -------
e: 44538
t: 29493
a: 25894
...
============= END ===============
```

If no argument is provided, the program will print usage instructions and exit:

```
Usage: python3 main.py <path_to_book>
```

## Configuration

No environment variables are required to run bookbot.

| Variable | Description |
|---|---|
| *(none)* | This project has no required environment variables. |

## Limitations

- **Plain text only** – BookBot only supports `.txt` files. PDF, EPUB, HTML, and other formats are not supported.
- **Alphabetic characters only** – The character frequency report filters to letters (a–z) and does not count digits, punctuation, or whitespace.
- **English-centric** – Word splitting is done on whitespace, which may not work correctly for languages that don't use spaces between words (e.g. Chinese, Japanese).
- **No encoding detection** – Files are read as UTF-8; books saved in other encodings (e.g. Latin-1, Windows-1252) will raise a `UnicodeDecodeError`.
