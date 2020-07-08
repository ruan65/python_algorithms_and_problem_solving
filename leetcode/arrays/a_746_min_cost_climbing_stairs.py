class Solution:
    def minCostClimbingStairs(self, cost: [int]) -> int:
        p = cost[0]
        pp = 0

        for pr in cost[1:]:
            curr = pr + min(p, pp)
            pp = p
            p = curr

        return min(p, pp)


if __name__ == '__main__':
    steps = [1, 3, 1, 1, 5]
    print(Solution().minCostClimbingStairs(steps))
