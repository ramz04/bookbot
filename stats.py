from typing import TypedDict

def count_num_of_words(get_book_text, path):
    book_text = get_book_text(path)
    return len(book_text.split())

def character_count(get_book_text, path):
    book_text = get_book_text(path)
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

def get_count(char_count: CharacterCount) -> int:
    return char_count["count"]

def sorted_char_count_dict(char_count: dict) -> list[CharacterCount]:
    char_count_list = [{"character": k, "count": v} for k, v in char_count.items()]
    char_count_list.sort(key=get_count, reverse=True)
    return char_count_list
