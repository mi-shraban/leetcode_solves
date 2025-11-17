class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ans = 0
        for x in nums:
            while stack and stack[-1] > x:
                stack.pop()
            if x == 0:
                continue
            if not stack or stack[-1] < x:
                ans += 1
                stack.append(x)
        return ans