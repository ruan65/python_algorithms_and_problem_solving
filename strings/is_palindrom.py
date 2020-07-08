def is_palindrome(text):
    size = len(text)
    a, b = text[:size // 2], text[(size + size % 2) // 2:]
    return a == b[::-1]


def is_pal_iter(s: str) -> bool:
    fw = 0
    bw = len(s) - 1

    while fw < bw:
        if s[fw] != s[bw]:
            return False
        fw += 1
        bw -= 1
    return True


is_palindrome('anna')
is_palindrome('anzyzna')

print(is_pal_iter(''))
print(is_pal_iter('anzyzna'))
