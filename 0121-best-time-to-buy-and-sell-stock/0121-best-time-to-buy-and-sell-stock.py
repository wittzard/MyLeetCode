class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # global
        max_profit = 0
        # local
        min_sofar = prices[0]

        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_sofar)
            min_sofar = min(min_sofar, prices[i])

        return max_profit