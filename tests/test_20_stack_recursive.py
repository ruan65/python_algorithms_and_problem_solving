from leetcode.parenthesis.a_20_valid_parenthesis_recurcive import is_balanced


def test_is_valid():
    assert is_balanced('{') is False
    assert is_balanced('') is True
    assert is_balanced(']') is False
    assert is_balanced('()[') is False
    assert is_balanced('}}()') is False
    assert is_balanced('[]') is True
    assert is_balanced("){") is False
    assert is_balanced("[()[[]()]]") is True
    assert is_balanced('([)]') is False
    assert is_balanced('[[[]]]()') is True
    assert is_balanced('[{[[]]}]{}[()[]]') is True
    assert is_balanced('{()()[()]}') is True
    assert is_balanced("(]") is False


