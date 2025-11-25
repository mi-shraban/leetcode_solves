class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k % 10 not in {1, 3, 7, 9}:
            return -1
        seen = set()
        n = 0
        for i in range(1, k+1):
            n = (n * 10 + 1) % k
            if n == 0:
                return i
            if n in seen:
                return -1
            seen.add(n)
        return -1        