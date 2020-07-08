def is_parth_sequence_valid(s: str) -> bool:
    if not s:
        return True
    if s.find('()') == -1:
        return False
    return is_parth_sequence_valid(s.replace('()', ''))


def is_valid(s: str) -> bool:
    stack = []
    for pr in s:
        if pr in ['(', '[', '{']:
            stack.append(pr)
        elif len(stack) == 0 or stack.pop() + pr not in ["()"]:
            return False
    return len(stack) == 0


class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:

        result = []
        md = ''
        if not s:
            return result
        for i in range(len(s)):
            if s[i] in ['(', ')']:
                md = s[:i] + s[i + 1:]

            if is_parth_sequence_valid(md):
                if md not in result:
                    result.append(md)
        return result


if __name__ == '__main__':
    # ps = "(a)())()"
    # print(Solution().removeInvalidParentheses(ps))

    sq = '(a)'
    print(is_valid(sq))
