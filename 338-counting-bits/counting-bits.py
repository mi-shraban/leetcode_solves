class Solution:
    def countBits(self, n: int) -> List[int]:
        def count_ones_kernighan(n):
            count = 0
            while n > 0:
                n &= (n - 1)
                count += 1
            return count
        return [count_ones_kernighan(i) for i in range(n+1)]
        # Kernighan's algo O(1). As binary representations can be at most 32/64 bits.