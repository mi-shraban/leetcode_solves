class Solution:
    def smallestNumber(self, n: int) -> int:
        ln = 0
        while n:
            n //= 2
            ln += 1
        return (2**ln)-1