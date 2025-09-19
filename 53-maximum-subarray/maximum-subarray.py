class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        r = nums[0]
        for i in range(1, len(nums)):
            r = max(r + nums[i], nums[i])
            ans = max(ans, r)
        return ans
        # O(n). Also solvable using divide and conquer, O(nlogn) time ;-;