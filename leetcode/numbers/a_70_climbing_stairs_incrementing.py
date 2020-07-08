class Solution:

    def climbStairs(self, n: int) -> int:

        if n == 1:
            return 1
        if n == 2:
            return 2

        one_before = 2
        two_before = 1
        all_way = 0

        for i in range(2, n):
            all_way = one_before + two_before
            two_before = one_before
            one_before = all_way
        return all_way


if __name__ == '__main__':
    print(Solution().climbStairs(20))
