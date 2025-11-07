class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        prefix = [0]
        for x in stations:
            prefix.append(prefix[-1] + x)
        for i in range(n):
            stations[i] = prefix[min(i+r+1, n)] - prefix[max(0, i-r)]
        def check(mnP):
            diff = [0]*n
            curr = 0
            cnt = 0
            for i, x in enumerate(stations):
                curr += diff[i]
                pwr_diff = mnP - x - curr
                if pwr_diff > 0:
                    cnt += pwr_diff
                    if cnt > k:
                        return False
                    curr += pwr_diff
                    if i + 2 * r + 1 < n:
                        diff[i + 2 * r + 1] -= pwr_diff
            return True
        lo = min(stations)
        hi = lo + k
        while lo <= hi:
            mid = lo + (hi-lo)//2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        return hi