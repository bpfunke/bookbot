def get_book_wc(book_text):
    return len(book_text.split())
    
def get_char_dict(book_text):
    char_dict = {}
    for txt in list(book_text.lower()):
        char_dict[txt] = char_dict.get(txt, 0) + 1
    return char_dict

def get_num(items):
    return items["num"]


def sort_char_dict (char_dict):
    char_details = {}
    sorted_char = []
    for char in char_dict:
        char_details["char"] = char
        char_details["num"] = char_dict[char]
        sorted_char.append(char_details.copy())
    sorted_char.sort(reverse=True, key=get_num)
    return sorted_char