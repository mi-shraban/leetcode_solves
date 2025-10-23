class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        lp = -10**9+7
        cnt = 0
        for x in nums:
            lb = x - k
            ub = x + k
            if lp < lb:
                lp = lb
            else:
                lp += 1
            if lp <= ub:
                cnt += 1
            else:
                lp -= 1
        return cnt