class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        frq = {}
        for x in nums:
            frq[x] = frq.get(x, 0) + 1
        for x in frq.values():
            if x > 2:
                return False
        return True