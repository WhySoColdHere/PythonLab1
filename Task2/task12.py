def sort_symbols(string: str):
    return ''.join(list(filter(lambda x: x.isdigit(), string)) + list(filter(lambda x: x.isalpha(), string)))

