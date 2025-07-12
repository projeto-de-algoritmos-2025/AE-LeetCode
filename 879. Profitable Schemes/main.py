class Solution:
    def profitableSchemes(self, n, minProfit, group, profit):
        MOD = 10**9 + 7
        G, P = len(group), minProfit
        dp = [[0] * (P + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for g, p in zip(group, profit):
            for people in range(n, g - 1, -1):
                for curr_profit in range(P, -1, -1):
                    next_profit = min(P, curr_profit + p)
                    dp[people][next_profit] = (dp[people][next_profit] + dp[people - g][curr_profit]) % MOD

        return sum(dp[people][P] for people in range(n + 1)) % MOD