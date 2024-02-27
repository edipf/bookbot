def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    count = count_words(text)
    print(f"--- Begin report of {path} ---")
    print(f"{count} words found in the document")
    print()
    dict = count_each_letter(text)
    sorted_dict = char_sorted_dict(dict)

    for dict in sorted_dict:
        if dict['char'].isalpha():
            print(f"The '{dict['char']}' character was found {dict['count']} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_each_letter(text):
    letters = {}
    for char in text:
        char = char.lower()
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def char_sorted_dict(dict):
    sorted_dict = []
    for ch in dict:
        sorted_dict.append({"char": ch, "count": dict[ch]})
    sorted_dict.sort(reverse=True, key=sort_on)
    return sorted_dict

main()