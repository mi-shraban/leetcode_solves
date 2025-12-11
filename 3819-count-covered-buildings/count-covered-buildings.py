class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rt = [0] * (n + 1)      # row top
        rb = [n + 1] * (n + 1)  # row bottom
        cl = [0] * (n + 1)      # column left
        cr = [n + 1] * (n + 1)  # column right
        for x, y in buildings:
            if x > rt[y]:
                rt[y] = x
            if x < rb[y]:
                rb[y] = x
            if y > cl[x]:
                cl[x] = y
            if y < cr[x]:
                cr[x] = y
        ans = 0
        for x, y in buildings:
            if rb[y] < x < rt[y] and cr[x] < y < cl[x]:
                ans += 1
        return ans