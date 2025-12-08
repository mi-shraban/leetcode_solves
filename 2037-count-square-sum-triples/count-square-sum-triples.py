class Solution:
    def countTriples(self, n: int) -> int:
        ans = 0
        for a in range(1, n):
            for b in range(a + 1, n):
                c = (a*a + b*b)**0.5
                if c == int(c) and c <= n:
                    ans += 2
        return ans
                