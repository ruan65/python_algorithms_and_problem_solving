def is_palindrome(text):
    size = len(text)
    a, b = text[:size // 2], text[(size + size % 2) // 2:]
    return a == b[::-1]


is_palindrome('anna')
is_palindrome('anyna')
