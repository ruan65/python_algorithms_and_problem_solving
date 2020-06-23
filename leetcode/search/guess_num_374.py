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


def give_variant(s, e):
    v = (s + e) // 2
    if v == s:
        return e
    if v == e:
        return s
    return v


guessed: int = 1

# end = 2147483647


class Solution:
    start = 1
    end = 2147483647


    def guessNumber(self, n: int) -> int:
        if guess(n) == 0:
            return n

        while True:
            if guess(self.start) == 0:
                return self.start

            if guess(self.end) == 0:
                return self.end

            n = give_variant(self.start, self.end)
            if guess(n) == 0:
                return n
            elif guess(n) > 0:
                self.start = n
            else:
                self.end = n





print(Solution().guessNumber(2))
