def get_book_wc(filepath):
    with open(filepath) as f:
        words = f.read().split()
    return len(words)
    
def get_book_cc(filepath):
    book_dict = {}
    with open(filepath) as f:
        book_txt = f.read().lower()
    for txt in list(book_txt):
        if txt in book_dict:
            book_dict[txt] += 1
        else:
            book_dict[txt] = 1
    return book_dict
