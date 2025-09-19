class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curs = mxs = sum(nums[:k])
        for i in range(k, len(nums)):
            curs += nums[i] - nums[i - k]
            mxs = max(mxs, curs)
        return mxs/k