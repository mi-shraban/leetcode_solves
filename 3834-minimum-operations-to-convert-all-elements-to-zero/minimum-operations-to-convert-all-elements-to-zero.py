class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = [0] * (len(nums)+1)
        ans = 0
        top = 0
        for x in nums:
            while stack[top] > x:
                top -= 1
                ans += 1
            if stack[top] !=  x:
                top += 1
                stack[top] = x
        return ans + top