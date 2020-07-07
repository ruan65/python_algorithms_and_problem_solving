class Solution:
    """
    @param coins: a list of integer
    @param amount: a total amount of money amount
    @return: the fewest number of coins that you need to make up
    """

    def coinChange(self, coins, amount):

        # EDGE CASE
        if amount == 0:
            return 0

        # INIT DIMENSIONS
        coin_row = len(coins) + 1
        amount_col = amount + 1

        # BY DEFAULT, 2**64 DENOTES IMPOSSIBLE TO MAKE CHANGE
        dp = [[2 ** 64 for _ in range(amount_col)] for _ in range(coin_row)]

        # BY DEFAULT, IF AMOUNT = 0, WE NEED EXACTLY 0 COINS
        for coin in range(coin_row):
            dp[coin][0] = 0

        # OTHER CELLS
        for coin in range(1, coin_row):
            for am in range(1, amount_col):

                # CASE 1 - WE MUST LEAVE THE COIN
                if am < coins[coin - 1]:
                    dp[coin][am] = dp[coin - 1][am]

                # CASE 2 - WE CAN TAKE OR LEAVE THE COIN
                else:
                    take = 1 + dp[coin][am - coins[coin - 1]]
                    leave = dp[coin - 1][am]
                    dp[coin][am] = min(take, leave)

        for row in dp:
            print(row)

        return -1 if dp[-1][-1] == 2 ** 64 else dp[-1][-1]

print(Solution().coinChange([1,2, 5], 6))