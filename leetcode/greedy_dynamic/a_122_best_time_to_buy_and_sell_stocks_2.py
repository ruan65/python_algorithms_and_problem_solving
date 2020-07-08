class Solution:
    def maxProfit(self, prices: [int]) -> int:
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == '__main__':
    pr_list = [2, 8, 2, 10, 0, 1, 2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
