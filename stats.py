def get_book_wc(filepath):
    with open(filepath) as f:
        words = f.read().split()
    return len(words)
    
def get_book_cc(filepath):
    char_dict = {}
    with open(filepath) as f:
        book_txt = f.read().lower()
    for txt in list(book_txt):
        char_dict[txt] = char_dict.get(txt, 0) + 1
    return char_dict

def get_num(items):
    return items["num"]


def sorted_cc (filepath):
    char_details = {}
    sorted_char = []
    char_dict = get_book_cc(filepath)
    for char in char_dict:
        if char.isalpha():
            char_details["char"] = char
            char_details["num"] = char_dict[char]
            sorted_char.append(char_details.copy())
    sorted_char.sort(reverse=True, key=get_num)
    return sorted_char