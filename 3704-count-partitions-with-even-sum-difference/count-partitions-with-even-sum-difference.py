class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        ans = 0
        for i in range(n-1):
            diff = nums[i] - (nums[n - 1] - nums[i])
            if diff % 2 == 0:
                ans += 1
        return ans