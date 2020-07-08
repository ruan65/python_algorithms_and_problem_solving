# Approach #1: Dynamic Programming [Accepted]
# Intuition and Algorithm
#
# At the end of the i-th day, we maintain cash, the maximum profit we could have if we did not
# have a share of stock, and hold, the maximum profit we could have if we owned a share of stock.
#
# To transition from the i-th day to the i+1-th day, we either sell our stock
# cash = max(cash, hold + prices[i] - fee) or buy a stock hold = max(hold, cash - prices[i]).
# At the end, we want to return cash.
# We can transform cash first without using temporary variables because selling
# and buying on the same day can't be better than just continuing to hold the stock.


class Solution:
    def maxProfit(self, pr: [int], fee: int) -> int:
        cash, hold = 0, -pr[0]
        for i in range(1, len(pr)):
            cash = max(cash, hold + pr[i] - fee)
            hold = max(hold, cash - pr[i])
        return cash

if __name__ == '__main__':
    pr_list = [2, 8, 2, 10, 0, 1, 2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
