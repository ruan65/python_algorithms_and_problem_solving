from ya.anagrams import is_anagram, string_to_dict


def test_is_anagram():
    # True
    assert is_anagram('ala', 'ala') is True
    assert is_anagram('', '') is True
    assert is_anagram('a', 'a') is True
    assert is_anagram('aa', 'aa') is True
    assert is_anagram('ab', 'ba') is True
    # False
    assert is_anagram('ab', 'ca') is False
    assert is_anagram('a', 'c') is False
    assert is_anagram('', 'c') is False
    assert is_anagram('aba', 'abaa') is False
    assert is_anagram('abas', 'aba') is False
    assert is_anagram('aa', 'aaa') is False


def test_string_to_dict():
    assert string_to_dict('ab') == {'a': 1, 'b': 1}
    assert string_to_dict('aaab') == {'a': 3, 'b': 1}
    assert string_to_dict('abb') == {'a': 1, 'b': 2}
    assert string_to_dict('') == {}
