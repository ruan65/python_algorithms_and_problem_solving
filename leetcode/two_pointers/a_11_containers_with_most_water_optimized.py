class Solution:

    def maxArea(self, height: [int]) -> int:

        mv = 0
        s, e = 0, len(height) - 1

        while s != e:
            hs = height[s]
            he = height[e]
            vl = (e - s) * min(hs, he)
            if mv < vl:
                mv = vl
            if hs <= he:
                s += 1
                continue
            if he <= hs:
                e -= 1
        return mv


if __name__ == '__main__':
    inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    # s = 1
    # f = 8
    # print(area((s, inp[s]), (f, inp[f])))
    print(Solution().maxArea(inp))
