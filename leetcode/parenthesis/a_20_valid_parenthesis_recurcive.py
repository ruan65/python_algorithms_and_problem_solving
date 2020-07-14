p1, p2, p3 = '()', '{}', '[]'


class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if s.find(p1) + s.find(p2) + s.find(p3) == -3:
            return False
        return self.isValid(s.replace(p1, '').replace(p2, '').replace(p3, ''))

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
