class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mn = 10**6+7
        ans = 0
        for x in prices:
            if mn > x:
                mn = x
            profit = x - mn
            if ans < profit:
                ans = profit
        return ans
        # mn = min(mn, x)
        # ans = max(ans, (x - mn))
        # using min max function is much slower ;-;