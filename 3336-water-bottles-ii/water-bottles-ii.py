class Solution:
    def maxBottlesDrunk(self, b: int, n: int) -> int:
        ans = b
        while b >= n:
            b -= n - 1
            n += 1
            ans += 1
        return ans