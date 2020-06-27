def closer(x):
    return {'(': ')',
            '{': '}',
            '[': ']'}[x]


def is_closer_for(o, c) -> bool:
    return c == closer(o)


def is_opener(b: str) -> bool:
    return b in ['(', '{', '[']


def is_closer(b: str) -> bool:
    return b in [')', '}', ']']


def is_match_closer(o: str, c: str) -> bool:
    return is_opener(o) and is_closer_for(o, c)


def is_parenth_sequence_correct(sq: str) -> bool:
    if sq == '':
        return True
    if len(sq) % 2 == 1 or not is_opener(sq[0]) or not is_closer(sq[-1]):
        return False
    stack: [str] = []

    for c in sq:
        if is_opener(c):
            stack.append(c)
        elif is_closer(c) and not len(stack) == 0 and is_match_closer(stack[-1], c):
            stack.pop()

    return len(stack) == 0


def is_valid(s: str) -> bool:
    stack = []
    for i in s:
        if i in ['(', '[', '{']:
            stack.append(i)
        elif len(stack) == 0 or stack.pop() + i not in ["()", "[]", "{}"]:
            return False
    return len(stack) == 0


class Solution:
    def isValid(self, s: str) -> bool:
        return is_parenth_sequence_correct(s)


if __name__ == '__main__':
    # print(split_last_closer('((){}[()])]'))

    # print(is_parenth_sequence_correct("[()[[]()]]"))

    print(is_parenth_sequence_correct('[{[[]]}]{}[()[]]'))
