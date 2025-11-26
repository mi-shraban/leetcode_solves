class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[[0] * k for _ in range(m)] for _ in range(n)]
        dp[0][0][grid[0][0] % k] = 1
        for i in range(n):
            for j in range(m):
                for x in range(k):
                    if j > 0:
                        dp[i][j][(x + grid[i][j]) % k] += dp[i][j - 1][x] % mod
                    if i > 0:
                        dp[i][j][(x + grid[i][j]) % k] += dp[i - 1][j][x] % mod
        return dp[-1][-1][0] % mod
