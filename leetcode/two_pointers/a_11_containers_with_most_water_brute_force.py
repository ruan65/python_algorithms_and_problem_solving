def area(siv: (int, int), fiv: (int, int)) -> int:
    return (fiv[0] - siv[0]) * min(fiv[1], siv[1])


class Solution:

    def maxArea(self, height: [int]) -> int:

        mv = 0

        for i in range(len(height) - 1):
            for j in range(1, len(height)):
                vl = area((i, height[i]), (j, height[j]))
                if mv < vl:
                    mv = vl
        return mv


if __name__ == '__main__':
    inp = [3, 2, 8]
    # s = 1
    # f = 8
    # print(area((s, inp[s]), (f, inp[f])))
    print(Solution().maxArea(inp))
