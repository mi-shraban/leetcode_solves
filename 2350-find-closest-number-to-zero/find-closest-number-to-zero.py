class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = 10**6+7
        for x in nums:
            ans = min(abs(x), ans)
        return ans if ans in nums else -ans