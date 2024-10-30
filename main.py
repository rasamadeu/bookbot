def main():
    path = "books/frankenstein.txt"
    text = read_book(path)
    words = count_words(text)
    characters = count_characters(text)
    book_report(path, words, characters)


def read_book(path):
    with open(path, "r") as f:
        text = f.read()
    return text


def count_words(text):
    return len(text.split())


def count_characters(text):
    characters = {}

    for char in text:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters


def sort_characters(char_dict):
    return -char_dict["count"]


def book_report(path, words, characters):

    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()

    # Process characters dictionary
    char_list = []
    for char in characters:
        if char.isalpha():
            char_list.append({"char": char, "count": characters[char]})
    char_list.sort(key=sort_characters)

    for i in char_list:
        print(f"The {i['char']} character was found {i['count']} times")
    print("--- End report ---")


if __name__ == "__main__":
    main()
