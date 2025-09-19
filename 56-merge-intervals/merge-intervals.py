class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for x, y in intervals:
            if not ans or ans[-1][1] < x:
                ans.append([x, y])
            else:
                ans[-1][1] = max(ans[-1][1], y)
        return ans