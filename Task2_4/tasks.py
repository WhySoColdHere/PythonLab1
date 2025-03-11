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


def sort_symbols(string: str):
    return ''.join(list(filter(lambda x: x.isdigit(), string)) + list(filter(lambda x: x.isalpha(), string)))


def shuffle_words_again(string):
    spl_string = string.split(' ')
    shuffle(spl_string)
    return ' '.join(spl_string)


tasks = {'6': shuffle_words, "12": sort_symbols, "13": shuffle_words_again}
task = input("Enter task, you wanna solve (6, 12, 13): ")
task_data = input("Enter task data: ")
print("\n")

try:
    print(tasks[task](task_data))
except KeyError:
    print("Task number is incorrect, try again.")
