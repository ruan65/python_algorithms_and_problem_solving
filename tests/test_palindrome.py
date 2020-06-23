from ya.palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome('hh') is True
    assert is_palindrome('') is True
    assert is_palindrome('huh') is True
    assert is_palindrome('huhu') is False
    assert is_palindrome('hu1uh') is True
    assert is_palindrome('hu1hu') is False
