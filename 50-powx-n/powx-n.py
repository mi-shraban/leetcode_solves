class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        ans = 1
        pwr = abs(n)
        while pwr:
            if pwr & 1:
                ans *= x
            x *= x
            pwr //= 2
        return ans if n >= 0 else 1 / ans