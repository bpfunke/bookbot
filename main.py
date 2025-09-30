from stats import get_book_wc
from stats import get_book_cc

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    #print(get_book_text(file_path))
    print(f"Found {get_book_wc(file_path)} total words")
    print(get_book_cc(file_path))

main()
