class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = -10**9+7
        cnt = 0
        for x in nums:
            lb = x - k      # lowerbound
            ub = x + k      # upperbound
            if curr < lb:
                curr = lb
            else:
                curr += 1
            if curr <= ub:
                cnt += 1
            else:
                curr -= 1
        return cnt