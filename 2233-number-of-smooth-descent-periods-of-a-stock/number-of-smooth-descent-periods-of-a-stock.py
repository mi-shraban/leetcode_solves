class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans, cnt = 1, 1
        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1] == 1:
                cnt += 1
            else:
                cnt = 1
            ans += cnt
        return ans