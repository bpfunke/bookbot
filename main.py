from stats import get_book_wc
from stats import get_book_cc
from stats import sorted_cc

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    #print(get_book_text(file_path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_book_wc(file_path)} total words")
    print("--------- Character Count -------")
    char_list = sorted_cc(file_path)
    for char in char_list:
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")

main()
