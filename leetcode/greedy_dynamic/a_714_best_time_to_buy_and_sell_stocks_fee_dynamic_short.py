class Solution:
    def maxProfit(self, pr: [int], fee: int) -> int:
        if not pr or len(pr) < 2:
            return 0
        profit = 0
        bp = pr[0]

        for i in range(1, len(pr)):
            if pr[i] < bp:
                bp = pr[i]
            elif pr[i] > bp + fee:
                profit += pr[i] - bp - fee
                bp = pr[i] - fee
        return profit


if __name__ == '__main__':
    pr_list = [2, 8, 2, 10, 0, 1, 2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
