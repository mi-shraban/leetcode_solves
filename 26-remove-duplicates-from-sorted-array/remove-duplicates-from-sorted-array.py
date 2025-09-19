class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        for x in nums:
            if x!= nums[idx]:
                idx += 1
                nums[idx] = x
        return idx + 1