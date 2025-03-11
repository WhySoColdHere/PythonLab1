def is_simple(number):
    number = abs(number)
    if number < 2:
        return False
    for sub_number in range(2, int(number ** 0.5) + 1):
        if number % sub_number == 0:
            return False
    return True


def choose_task(task_numbers: list, task_funcs: list):
    tasks = dict()
    for task_number, task_func in zip(task_numbers, task_funcs):
        tasks[task_number] = task_func

    task = input(f"Enter task, you wanna solve {', '.join(task_numbers)}: ")
    task_data = input("Enter task data: ")
    print("\n")

    try:
        return tasks[task](task_data)
    except KeyError:
        print("Task number is incorrect, try again.")
        return "Error"


def list_of_strings_input():
    strings = []
    string = "str"
    while string != '':
        string = input()
        strings.append(string)
    return strings[0:-1]
