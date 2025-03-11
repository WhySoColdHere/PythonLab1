from re import findall
from common_funcs import choose_task


def nums_greater_then_5(string):
    return len(list(filter(lambda x: int(x) > 5, findall(r'\d+', string))))


def get_unused_cyrillic_symbols(string):
    start = 1040
    end = 1103

    all_cyrillic_chars = set()
    for codepoint in range(start, end + 1):
        all_cyrillic_chars.add(chr(codepoint))  # chr(int) преобразует кодовую точку в Unicode символ
    return list(all_cyrillic_chars - set(string))


def bigger_natural_number(string):
    try:
        return max(list(map(lambda x: int(x), filter(lambda x: int(x) > 1, findall(r'\d+', string)))))
    except ValueError:
        return 0


print(choose_task(
    ['6', "12", "13"],
    [nums_greater_then_5, get_unused_cyrillic_symbols, bigger_natural_number])
)
