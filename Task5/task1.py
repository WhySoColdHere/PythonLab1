import re


def get_date(string):
    pattern = r'\b(\d{1,2})\s+([А-ЯЁа-яё]+)\s+(\d{4})\b'
    return re.findall(pattern, string)
