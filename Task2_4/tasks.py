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


tasks = {'6': shuffle_words}
task = input("Enter task, you wanna solve (6, 12, 13): ")
task_data = input("Enter task data: ")

try:
    print('\n' + tasks[task](task_data))
except KeyError:
    print("Task number is incorrect, try again.")
