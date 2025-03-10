from common_funcs import is_simple


def func1(n):
    res = 0
    for sub_num in range(2, int(n ** 0.5) + 1):
        if n % sub_num == 0:
            first_divider = sub_num
            second_divider = n // sub_num
            res += first_divider if not is_simple(first_divider) else 0
            res += second_divider if not is_simple(second_divider) and first_divider != second_divider else 0
    return res + 1 + n if not is_simple(n) else res + 1
