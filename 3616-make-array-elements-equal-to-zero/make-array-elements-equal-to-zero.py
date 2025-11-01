class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        l, r = 0, sum(nums)
        for i in range(n):
            l += nums[i]
            r -= nums[i]
            if nums[i] != 0:
                continue
            if l == r:
                ans += 2
            if abs(l - r) == 1:
                ans += 1
        return ans