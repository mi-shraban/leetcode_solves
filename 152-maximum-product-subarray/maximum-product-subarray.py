class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = -10**18
        l = r = 1
        n = len(nums)
        for i in range(n):
            l *= nums[i]
            r *= nums[n-i-1]
            ans = max(ans, l, r)
            if l == 0:
                l = 1
            if r == 0:
                r = 1
        return ans