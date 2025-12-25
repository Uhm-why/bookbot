import sys

from stats import dict_to_list, get_char_count, get_word_count


def get_book_text(file_path):
    book_contents = None
    with open(file_path, "r") as book:
        book_contents = book.read()

    return book_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_contents = get_book_text(sys.argv[1])
    word_count = get_word_count(book_contents)
    char_dict = get_char_count(book_contents)
    char_list = dict_to_list(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char in char_list:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")


main()
