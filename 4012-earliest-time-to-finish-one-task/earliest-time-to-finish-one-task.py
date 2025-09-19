class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        ans = 10**6
        for x, y in tasks:
            if ans > x + y:
                ans = x + y
        return ans
        # ans = min(x+y, ans) # it be slow ;-;