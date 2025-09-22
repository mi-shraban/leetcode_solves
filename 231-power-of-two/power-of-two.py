class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        count = 0
        while n > 0:
            count += (n & 1)
            n >>= 1
            if count > 1:
                return False
        return True