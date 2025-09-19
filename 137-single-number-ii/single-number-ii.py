class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = 0
        twos = 0
        for x in nums:
            ones ^= (x & ~twos)
            twos ^= (x & ~ones)
        return ones