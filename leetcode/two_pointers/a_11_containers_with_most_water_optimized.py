class Solution:

    def maxArea(self, h: [int]) -> int:

        mx, st, end = 0, 0, len(h) - 1

        while st < end:
            curr = min(h[st], h[end]) * (end - st)
            mx = max(mx, curr)

            if h[st] < h[end]:
                st += 1
            else:
                end -= 1
        return mx


if __name__ == '__main__':
    inp = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(Solution().maxArea(inp)) # 49
