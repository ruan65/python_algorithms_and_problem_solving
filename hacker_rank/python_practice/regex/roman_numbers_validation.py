import re


def is_correct_roman_num(s: str) -> bool:
    pattern = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$')
    return re.match(pattern, s) is not None
