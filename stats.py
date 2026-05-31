from typing import TypedDict

def count_num_of_words(get_book_text):
    print("Counting number of words...")
    book_text = get_book_text("./books/frankenstein.txt")
    words = book_text.split()
    nums_of_words = len(words)
    print(f"Found {nums_of_words} total words")


def character_count(get_book_text):
    print("Counting number of characters...")
    book_text = get_book_text("./books/frankenstein.txt")
    char_count = {}
    for char in book_text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

class CharacterCount(TypedDict):
    character: str
    count: int

def sorted_char_count_dict(char_count:dict) -> list[CharacterCount]:
    