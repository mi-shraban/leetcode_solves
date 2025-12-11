class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rt = [0] * (n + 1)
        rb = [n + 1] * (n + 1)
        cl = [0] * (n + 1)
        cr = [n + 1] * (n + 1)
        for x, y in buildings:
            rt[y] = max(rt[y], x)
            rb[y] = min(rb[y], x)
            cl[x] = max(cl[x], y)
            cr[x] = min(cr[x], y)
        ans = 0
        for x, y in buildings:
            if rb[y] < x < rt[y] and cr[x] < y < cl[x]:
                ans += 1
        return ans