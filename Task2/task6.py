from random import shuffle


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

