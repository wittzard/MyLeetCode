import math

class Solution:
    def maxProfitDP(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        profit = -math.inf

        # local
        dp = [0]*n
        dp[0] = prices[0]

        for i in range(1,n):
            dp[i] = min(dp[i-1], prices[i])
            profit = max(profit, prices[i]-dp[i])

        return profit

    # reduce space
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0

        profit = -math.inf
        min_sofar = prices[0]

        for i in range(1,n):
            min_sofar = min(min_sofar, prices[i])
            profit = max(profit, prices[i] - min_sofar)

        return profit


        