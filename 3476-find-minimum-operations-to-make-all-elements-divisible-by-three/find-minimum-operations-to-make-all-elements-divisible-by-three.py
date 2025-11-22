class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        for i in range(n):
            if nums[i] % 3 == 0:
                ans -= 1
        return ans