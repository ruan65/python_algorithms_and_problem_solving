from leetcode.parenthesis.a_20_valid_parenthesis_stack import is_parenth_sequence_correct, is_valid


def test_is_parenth_sequence_correct():
    assert is_parenth_sequence_correct('') is True
    assert is_parenth_sequence_correct('{') is False
    assert is_parenth_sequence_correct(']') is False
    assert is_parenth_sequence_correct('()[') is False
    assert is_parenth_sequence_correct('}}()') is False

    assert is_parenth_sequence_correct('[]') is True
    assert is_parenth_sequence_correct("){") is False

    assert is_parenth_sequence_correct("[()[[]()]]") is True
    #
    assert is_parenth_sequence_correct('([)]') is False
    assert is_parenth_sequence_correct('[[[]]]()') is True
    assert is_parenth_sequence_correct('[{[[]]}]{}[()[]]') is True
    assert is_parenth_sequence_correct('{()()[()]}') is True
    assert is_parenth_sequence_correct("(]") is False


def test_is_valid():
    assert is_valid('') is True
    assert is_valid('{') is False
    assert is_valid(']') is False
    assert is_valid('()[') is False
    assert is_valid('}}()') is False

    assert is_valid('[]') is True
    assert is_valid("){") is False

    assert is_valid("[()[[]()]]") is True
    #
    assert is_valid('([)]') is False
    assert is_valid('[[[]]]()') is True
    assert is_valid('[{[[]]}]{}[()[]]') is True
    assert is_valid('{()()[()]}') is True
    assert is_valid("(]") is False


