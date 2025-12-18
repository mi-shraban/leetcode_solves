class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        strategic_prices = [s * p for s, p in zip(strategy, prices)]
        profit = sum(strategic_prices)
        new_profit = profit
        for i in range(k):
            new_profit -= strategy[i] * prices[i]
            if i >= k//2:
                new_profit += prices[i]
        if new_profit > profit:
            profit = new_profit
        for i in range(n-k):
            new_profit -= (strategy[i + k] - 1) * prices[i + k]
            new_profit += strategy[i] * prices[i]
            new_profit -= prices[i + k//2]
            if new_profit > profit:
                profit = new_profit
        return profit