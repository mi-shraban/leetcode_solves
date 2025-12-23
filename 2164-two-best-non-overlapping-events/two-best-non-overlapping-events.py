class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        schedule = []
        ans = m = 0
        for s, e, v in events:
            schedule.append((s, True, v))
            schedule.append((e + 1, False, v))
        schedule.sort()
        for t, s, v in schedule:
            if s:
                ans = max(ans, m + v)
            else:
                m = max(m, v)
        return ans