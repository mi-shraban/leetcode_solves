class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        f1, f2 = 0, 1
        for i in range(2, n+1):
            ans = f1 + f2
            f1 = f2
            f2 = ans
        return ans