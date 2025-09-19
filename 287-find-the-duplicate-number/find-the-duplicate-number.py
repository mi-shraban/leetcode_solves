class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = [0]*(max(nums)+1)
        for x in nums:
            freq[x] += 1
            if freq[x] > 1:
                return x