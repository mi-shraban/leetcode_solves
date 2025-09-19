class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sm1 = sum(nums)
        sm2 = n*(n+1)//2
        return sm2-sm1  