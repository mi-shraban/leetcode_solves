class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        window = k - 1
        if window == 0:
            return True
        for i in range(k+1, len(nums)):
            if nums[i] > nums[i-1] and nums[i-k] > nums[i-k-1]:
                window -= 1
            else:
                window = k - 1
            if window == 0:
                return True
        return False