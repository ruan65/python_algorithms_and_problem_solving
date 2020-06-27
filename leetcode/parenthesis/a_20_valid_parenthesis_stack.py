def split_last_closer(d: str) -> (str, str):
    if len(d) == 0:
        return '', ''
    pattern = closer(d[0])
    i = d.rfind(pattern)
    return d[:i + 1], d[i + 1:]


def is_parenth_sequence_correct(sq: str) -> bool:
    if sq == '':
        return True
    if len(sq) % 2 == 1:
        return False
    if len(sq) == 2:
        if sq[0] not in ['(', '[', '{'] or sq[1] not in [')', ']', '}']:
            return False
        elif closer(sq[0]) == sq[1]:
            return True
        else:
            return False

    if sq[0] in [')', ']', '}'] or sq[len(sq) - 1] in ['(', '[', '{']:
        return False

    while len(sq) > 0:
        if is_closer(sq[0], sq[len(sq) - 1]):
            sq = pill(sq)
        else:
            l, r = split_last_closer(sq)
            return is_parenth_sequence_correct(l) and is_parenth_sequence_correct(r)

    return True


def pill(s: str):  # '[[]]'
    if len(s) < 3:
        return ''
    if is_closer(s[0], s[1]):
        return pill(s[2:])
    elif s[-2] in ['(', '[', '{'] and is_closer(s[-2], s[len(s) - 1]):
        return pill(s[:-2])
    else:
        return s[1:len(s) - 1]


def closer(x):
    return {'(': ')',
            '{': '}',
            '[': ']'}[x]


def is_closer(o, c) -> bool:
    return c == closer(o)


class Solution:
    def isValid(self, s: str) -> bool:
        return is_parenth_sequence_correct(s)


if __name__ == '__main__':
    # print(split_last_closer('((){}[()])]'))

    # print(is_parenth_sequence_correct("[()[[]()]]"))
    #
    print(f'pilled: {pill("[()[[]()]]")}')
