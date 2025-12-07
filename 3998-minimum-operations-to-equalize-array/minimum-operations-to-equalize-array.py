class Solution:
    def minOperations(self, nums: List[int]) -> int:
        return 1 if len(set(nums)) > 1 else 0