class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        l, cnt, mod = 0, 1, 10**9 + 7
        mxQ, mnQ, dp = deque(), deque(), [cnt]
        for r, x in enumerate(nums):
            while mxQ and x > nums[mxQ[-1]]:
                mxQ.pop()
            while mnQ and x < nums[mnQ[-1]]:
                mnQ.pop()
            mxQ.append(r)
            mnQ.append(r)
            while nums[mxQ[0]] - nums[mnQ[0]] > k:
                cnt -= dp[l]
                l += 1
                if l > mnQ[0]:
                    mnQ.popleft()
                if l > mxQ[0]:
                    mxQ.popleft()
            dp.append(cnt)
            cnt *= 2
            cnt %= mod
        return dp[-1] % mod