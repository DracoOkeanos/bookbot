
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

from stats import count_words, count_characters, sort_characters

def get_book_text(path):
    with open(path) as f:  
        return f.read()

def main():
    value = get_book_text(sys.argv[1]) 

    num_words = count_words(value) 
    print(f"Found {num_words} total words")

    char_counts = count_characters(value)  
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

main()


