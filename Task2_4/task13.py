from random import shuffle


def shuffle_words_again(string):
    spl_string = string.split(' ')
    shuffle(spl_string)
    return ' '.join(spl_string)

