class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9+7
        ht = {}
        for x, y in points:
            ht[y] = ht.get(y, 0) + 1
        ans = total = 0
        for y, cnt in ht.items():
            lines = cnt * (cnt - 1) // 2
            ans = (ans + total * lines) % mod
            total = (total + lines) % mod
        return ans
