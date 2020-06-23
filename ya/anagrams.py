import sys


def is_anagram(w1, w2):
    return string_to_dict(w1) == string_to_dict(w2)


def string_to_dict(text):
    result = {}
    for c in text:
        if c not in result:
            result[c] = 1
        else:
            result[c] += 1
    return result


text_1 = sys.stdin.readline().strip()
text_2 = sys.stdin.readline().strip()

if is_anagram(text_1, text_2):
    print(1)
else:
    print(0)
