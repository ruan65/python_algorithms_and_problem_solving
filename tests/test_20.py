from leetcode.parenthesis.a_20_valid_parenthesis import split_last_closer, is_parenth_sequence_correct, is_closer, pill


def test_split_parenth():
    assert split_last_closer('(){}') == ('()', '{}')
    assert split_last_closer('(){') == ('()', '{')
    assert split_last_closer('((){}[()])]') == ('((){}[()])', ']')
    assert split_last_closer('({') == ('', '({')
    assert split_last_closer('(') == ('', '(')
    assert split_last_closer('') == ('', '')


def test_is_parenth_sequence_correct():
    assert is_parenth_sequence_correct("[()[[]()]]") is True
    assert is_parenth_sequence_correct('') is True
    assert is_parenth_sequence_correct('[]') is True
    assert is_parenth_sequence_correct("){") is False

    assert is_parenth_sequence_correct('{') is False
    assert is_parenth_sequence_correct(']') is False
    assert is_parenth_sequence_correct('()[') is False
    #
    assert is_parenth_sequence_correct('([)]') is False
    assert is_parenth_sequence_correct('[[[]]]()') is True
    assert is_parenth_sequence_correct('[{[[]]}]{}[()[]]') is False
    assert is_parenth_sequence_correct('{()()[()]}') is False
    assert is_parenth_sequence_correct("(]") is False


def test_is_closer():
    assert is_closer('{', '}') is True
    assert is_closer('(', ')') is True
    assert is_closer('[', ']') is True
    assert is_closer('[', ')') is False


def test_pill():
    assert pill('()') == ''
    assert pill('()()') == ''

