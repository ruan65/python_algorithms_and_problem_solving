def is_valid(s: str) -> bool:
    count = 0
    for c in s:
        count += (c == '(') - (c == ')')
        if count < 0:
            return False
    return not count


class Solution:
    def removeInvalidParentheses(self, s: str) -> [str]:
        st = {s}

        while True:
            res = []
            for w in st:
                if is_valid(w):
                    res.append(w)
            if res:
                return res
            st2 = set()

            for w in st:
                for i in range(len(w)):
                    st2.add(w[:i] + w[i + 1:])
            print(st2)
            st = st2


if __name__ == '__main__':
    ps = "(a)(())"
    print(Solution().removeInvalidParentheses(ps))

    print(is_valid(ps))
