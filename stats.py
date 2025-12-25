def get_word_count(text):
    split_words = text.split()
    word_count = len(split_words)

    return word_count


def get_char_count(text):
    char_dict = {}

    for char in text:
        lower_char = char.lower()
        if lower_char in char_dict:
            char_dict[lower_char] += 1
        else:
            char_dict[lower_char] = 1

    return char_dict


def sort_on(characters):
    return characters["num"]


def dict_to_list(char_dict):
    char_list = []

    for chr in char_dict:
        if chr.isalpha():
            mini_char_dict = {"char": chr, "num": char_dict[chr]}
            char_list.append(mini_char_dict)

    char_list.sort(reverse=True, key=sort_on)

    return char_list
