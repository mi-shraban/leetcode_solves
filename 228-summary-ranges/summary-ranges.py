class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
                j += 1
            if nums[j] == nums[i]:
                ans.append(f"{nums[i]}")
            else:
                ans.append(f"{nums[i]}->{nums[j]}")
            i = j + 1
        return ans