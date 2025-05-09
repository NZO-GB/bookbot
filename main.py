from stats import book_to_words
from stats import chars_in_book
from stats import get_book_text
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

book_in_text = get_book_text(book_path)

def report(book_path):
    
    def sort_on(dict):
        return dict["num"]

    listed_dics = []

    chars_tmp = chars_in_book(book_in_text)

    for element in chars_tmp:
        listed_dics.append({"char":element, "num": chars_tmp[element]})

    listed_dics.sort(reverse = True, key = sort_on)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("------------ Word Count ----------")
    print(book_to_words(book_in_text))
    print("--------- Character Count -------")
    for element in listed_dics:
        print(f"{element['char']}: {element['num']}")
    print("============= END ===============")


report(book_path)
