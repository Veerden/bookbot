def main():
    book_path = "/home/keano/workspace/github.com/Veerden/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    chars_dict = get_chars_dict(text)
    book_report = get_char_report(chars_dict)
    print(book_report)
    


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_char_report(dict):
    char_list = []
    for char, num in dict.items():
        if char.isalpha() == True:
            char_list.append({'char': char, 'num': num})
    char_list.sort(key=lambda item: item['num'], reverse=True)
    for i in char_list:
        print(f"The '{i['char']}' character was found {i['num']} times")

    



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
