class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], -x[0]))
        ans = 0
        s, e = -1, -1   # start, end
        for l, r in intervals:
            if l > e:
                s = r - 1
                e = r
                ans += 2
            elif l > s:
                s = e
                e = r
                ans += 1
        return ans