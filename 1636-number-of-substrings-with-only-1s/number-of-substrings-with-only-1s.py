class Solution:
    def numSub(self, s: str) -> int:
        ans = 0
        mod = 10**9 + 7
        n = 0
        for x in s:
            if x == '1':
                n += 1
            else:
                ans += ((n * (n + 1)) // 2) % mod
                n = 0
        ans += ((n * (n + 1)) // 2) % mod
        return ans