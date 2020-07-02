# def maxProfit(self, prices: [int]) -> int:
#     one_buy = two_buy = sys.maxsize
#     one_profit = two_profit = 0
#     for p in prices:
#         one_buy = min(one_buy, p)
#         one_profit = max(one_profit, p - one_buy)
#         two_buy = min(two_buy, p - one_profit)
#         two_profit = max(two_profit, p - two_buy)
#     return two_profit

# class Solution:
#     def maxProfit(self, prices):
#         if not prices:
#             return 0
#
#         # forward traversal, profits record the max profit
#         # by the ith day, this is the first transaction
#         profits = []
#         max_profit = 0
#         current_min = prices[0]
#         for price in prices:
#             current_min = min(current_min, price)
#             max_profit = max(max_profit, price - current_min)
#             profits.append(max_profit)
#
#         # backward traversal, max_profit records the max profit
#         # after the ith day, this is the second transaction
#         total_max = 0
#         max_profit = 0
#         current_max = prices[-1]
#         for i in range(len(prices) - 1, -1, -1):
#             current_max = max(current_max, prices[i])
#             max_profit = max(max_profit, current_max - prices[i])
#             total_max = max(total_max, max_profit + profits[i])
#
#         return total_max
import sys


class Solution:
    def maxProfit(self, prices):
        first_buy = second_buy = sys.maxsize
        first_sell, second_sell = 0, 0
        for p in prices:
            first_buy = min(first_buy, p)
            first_sell = max(first_sell, p - first_buy)
            second_buy = min(second_buy, p - first_sell)
            second_sell = max(second_sell, p - second_buy)
            print(f'fb {first_buy} fp {first_sell} sb {second_buy} sp {second_sell}')
        return second_sell


if __name__ == '__main__':
    pr_list = [2, 8, 2, 1, 9, 10, 0, 1, 2]
    print(Solution().maxProfit(pr_list))
    # print(Solution().maxProfit(stock_prices))
