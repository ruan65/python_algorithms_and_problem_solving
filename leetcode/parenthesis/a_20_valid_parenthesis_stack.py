class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(': ')', '[': ']', '{': '}'}

        st = []

        for c in s:
            if c in mp.values():
                if not st or mp[st.pop()] != c:
                    return False
            elif c in mp:
                st.append(c)
        return not st



if __name__ == '__main__':
    # print(split_last_closer('((){}[()])]'))

    # print(is_parenth_sequence_correct("[()[[]()]]"))

    print(Solution().isValid('[{[[]]}]{}[()[]]'))
