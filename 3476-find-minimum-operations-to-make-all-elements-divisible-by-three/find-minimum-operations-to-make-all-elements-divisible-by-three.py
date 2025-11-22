class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            nums[i] = nums[i] % 3
            if nums[i] == 0:
                ans -= 1
        return ans