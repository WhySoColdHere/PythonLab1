from common_funcs import is_simple


def func3(n):
    def is_mutually_simple(num_1, num_2):
        while num_2:  # Алгоритм евклида
            num_1, num_2 = num_2, num_1 % num_2
        return num_1 == 1

    simple_nums_sum = sum((map(lambda x: int(x), filter(lambda x: is_simple(int(x)), str(n)))))

    counter = 0
    for sub_n in range(1, n):
        if n % sub_n != 0 and not is_mutually_simple(sub_n, n) and is_mutually_simple(sub_n, simple_nums_sum):
            counter += 1

    return counter


print(func3(int(input("Enter a number: "))))
