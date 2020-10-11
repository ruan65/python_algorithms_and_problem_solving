def bottom_up(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * i
    return dp[n]


def top_down(n):
    dp = [-1 for _ in range(n + 1)]

    def solve(x):
        if x == 0:
            return 1
        if dp[x] != -1:
            return dp[x]
        dp[x] = x * solve(x-1)
        return dp[x]

    solve(n)
    return dp[n]


if __name__ == '__main__':
    print(bottom_up(5))
    print(top_down(20))
