def is_simple(number):
    for sub_number in range(2, int(number ** 0.5) + 1):
        if number % sub_number == 0:
            return False
    return True
