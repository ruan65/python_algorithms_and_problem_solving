# recursive = out of time
# class Solution:
#     def climbStairs(self, n: int) -> int:
#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)

counter = 0


def count(n: int, hm: {int: int}) -> int:
    global counter
    counter += 1
    if n in hm:
        return hm[n]

    res = count(n - 1, hm) + count(n - 2, hm)
    hm[n] = res
    return res


class Solution:

    def climbStairs(self, n: int) -> int:
        hm = {1: 1, 2: 2}

        return count(n, hm)


if __name__ == '__main__':
    print(Solution().climbStairs(20))
    print(f'counter: {counter}')
