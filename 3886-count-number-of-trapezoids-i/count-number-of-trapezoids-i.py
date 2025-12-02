class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        mod = 10**9+7
        ht = {y:0 for x, y in points}
        for x, y in points:
            ht[y] += 1
        ans = total = 0
        for y, cnt in ht.items():
            if cnt < 2:
                continue
            lines = cnt * (cnt - 1) // 2
            ans = (ans + total * lines) % mod
            total = (total + lines) % mod
        return ans
