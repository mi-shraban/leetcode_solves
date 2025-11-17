class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        prev = None
        for i, x in enumerate(nums):
            if x == 1:
                if prev is not None and i - prev <= k:
                    return False
                prev = i
        return True