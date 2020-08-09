from hacker_rank.python_practice.regex.roman_numbers_validation import is_correct_roman_num


def test_is_correct_roman_num():
    # True
    assert is_correct_roman_num('I') is True
    assert is_correct_roman_num('III') is True
    assert is_correct_roman_num('XXX') is True
    assert is_correct_roman_num('VI') is True
    assert is_correct_roman_num('MMMCMXCIX') is True

    # False
    assert is_correct_roman_num('IIII') is False
    assert is_correct_roman_num('XXXX') is not True
