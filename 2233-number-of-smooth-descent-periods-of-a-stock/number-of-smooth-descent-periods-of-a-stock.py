class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, cnt, n = 1, 1, len(prices)
        for i in range(n - 1):
            if prices[i] - prices[i + 1] == 1:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans