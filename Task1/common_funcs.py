def is_simple(number):
    number = abs(number)
    if number < 2:
        return False
    for sub_number in range(2, int(number ** 0.5) + 1):
        if number % sub_number == 0:
            return False
    return True
