import sys
from stats import count_num_of_words, character_count, sorted_char_count_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(f"Found {count_num_of_words(get_book_text, book_path)} total words")
print("--------- Character Count -------")
for char_count in sorted_char_count_dict(character_count(get_book_text, book_path)):
    if char_count["character"].isalpha():
        print(f"{char_count['character']}: {char_count['count']}")
print("============= END ===============")
