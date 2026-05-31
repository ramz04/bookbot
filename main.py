from stats import count_num_of_words, character_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    print("Reading book...")
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

# main()
count_num_of_words(get_book_text)
print(character_count(get_book_text))
