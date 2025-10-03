from stats import ( get_book_wc, get_char_dict, sort_char_dict )
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(file_path, word_count, char_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        if char["char"].isalpha():
            print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    #file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_book_wc(book_text)
    char_count = get_char_dict(book_text)
    char_list = sort_char_dict(char_count)

    print_report(file_path, word_count, char_list)

    

main()
