from re import findall


def nums_greater_then_5(string):
    return len(list(filter(lambda x: int(x) > 5, findall(r'\d+', string))))


tasks = {'6': nums_greater_then_5}
task = input("Enter task, you wanna solve (6, 12, 13): ")
task_data = input("Enter task data: ")

try:
    print('\n' + tasks[task](task_data))
except KeyError:
    print("Task number is incorrect, try again.")
