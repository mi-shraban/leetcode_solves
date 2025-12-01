class Solution:
    def maxRunTime(self, n: int, b: List[int]) -> int:
        b.sort()
        sm = sum(b)
        while b[-1] > sm//n:
            n -= 1
            sm -= b.pop()
        return sm//n