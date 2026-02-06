class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # global 
        max_profit = 0

        # local 
        min_sofar = prices[0]

        for i in range(1, n):
            max_profit = max(max_profit, prices[i]-min_sofar)
            min_sofar = min(min_sofar, prices[i])
        
        return max_profit