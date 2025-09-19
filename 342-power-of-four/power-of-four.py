class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if not n & (n-1) and n % 3 == 1:
            return True
        return False
