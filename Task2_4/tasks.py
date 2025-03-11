from random import shuffle
from common_funcs import choose_task


def shuffle_words(string):
    def shuffle_word(word: str):
        sub_word = list(word[1: -1])
        shuffle(sub_word)
        return word[0] + ''.join(sub_word) + word[-1]

    splitted_string = string.split(' ')
    for i in range(len(splitted_string)):
        if len(splitted_string[i]) > 3:
            splitted_string[i] = shuffle_word(splitted_string[i])
    return ' '.join(splitted_string)


def sort_symbols(string: str):
    return ''.join(list(filter(lambda x: x.isdigit(), string)) + list(filter(lambda x: x.isalpha(), string)))


def shuffle_words_again(string):
    spl_string = string.split(' ')
    shuffle(spl_string)
    return ' '.join(spl_string)


print(choose_task(['6', '12', '13'], [shuffle_words, sort_symbols, shuffle_words_again]))
