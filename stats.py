def book_to_words(book):

    return f"Found {len(book.split())} total words"

def get_book_text(filepath):

    with open(filepath) as book:

        return book.read()

def chars_in_book(book):

    char_dict = {}
    for char in book.lower():
        if char in char_dict:
            char_dict[char] += 1
        else: char_dict[char] = 1

    return(char_dict)
