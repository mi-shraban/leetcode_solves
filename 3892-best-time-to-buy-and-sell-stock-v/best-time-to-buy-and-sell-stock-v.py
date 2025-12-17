class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        mn = -10**18 + 7
        n = len(prices)
        curr = [[mn] * 3 for i in range(k+1)]
        next_dp = [[mn] * 3 for i in range(k+1)]
        for i in range(k+1):
            next_dp[i][0] = 0
        for i in range(n-1, -1, -1):
            for j in range(k+1):
                curr[j][0] = next_dp[j][0]
                curr[j][0] = max(curr[j][0], next_dp[j][1] - prices[i])
                curr[j][0] = max(curr[j][0], next_dp[j][2] + prices[i])
                curr[j][1] = next_dp[j][1]
                curr[j][2] = next_dp[j][2]
                if j > 0:
                    curr[j][1] = max(curr[j][1], next_dp[j-1][0] + prices[i])
                    curr[j][2] = max(curr[j][2], next_dp[j-1][0] - prices[i])
            curr, next_dp = next_dp, curr
        return next_dp[k][0]