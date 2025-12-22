class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        dp = [1] * m
        for i in range(1, m):
            for j in range(i):
                ok = True
                for k in range(n):
                    if strs[k][j] > strs[k][i]:
                        ok = False
                        break
                if ok:
                    dp[i] = max(dp[i], dp[j] + 1)
        mx = 0
        for x in dp:
            mx = max(mx, x)
        return m - mx