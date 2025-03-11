from re import findall


def nums_greater_then_5(string):
    return len(list(filter(lambda x: int(x) > 5, findall(r'\d+', string))))


def get_unused_cyrillic_symbols(string):
    start = 1040
    end = 1103

    all_cyrillic_chars = set()
    for codepoint in range(start, end + 1):
        all_cyrillic_chars.add(chr(codepoint))  # chr(int) преобразует кодовую точку в Unicode символ
    return list(all_cyrillic_chars - set(string))


tasks = {'6': nums_greater_then_5, "12": get_unused_cyrillic_symbols}
task = input("Enter task, you wanna solve (6, 12, 13): ")
task_data = input("Enter task data: ")
print("\n")

try:
    print(tasks[task](task_data))
except KeyError:
    print("Task number is incorrect, try again.")
