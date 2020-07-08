import sys


class Solution:
    def maximumProduct(self, nums: [int]) -> int:
        mx1 = mx2 = mx3 = -sys.maxsize
        mn1 = mn2 = sys.maxsize

        for n in nums:
            if n > mx1:
                mx3 = mx2
                mx2 = mx1
                mx1 = n
            elif n > mx2:
                mx3 = mx2
                mx2 = n
            elif n > mx3:
                mx3 = n

            if n < mn1:
                mn2 = mn1
                mn1 = n
            elif n < mn2:
                mn2 = n
        return max(mx1 * mx2 * mx3, mx1 * mn1 * mn2)


if __name__ == '__main__':
    nms = [1, -1, 2, -5, 3]
    print(Solution().maximumProduct(nms))
