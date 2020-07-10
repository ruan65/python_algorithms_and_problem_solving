# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


def guess(num: int) -> int:
    if guessed > num:
        return 1
    elif guessed < num:
        return -1
    return 0

guessed: int = 100

# end = 2147483647


class Solution:
    def guessNumber(self, n):
        lo, hi = 1, n
        while lo < hi:
            mid = (lo + hi) // 2
            if guess(mid) == 1:
                lo = mid + 1
            else:
                hi = mid
        return lo





print(Solution().guessNumber(200000000))
