class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ht = {}
        for i, x in enumerate(nums):
            if x in ht and i - ht[x] <= k:
                return True
            ht[x] = i
        return False
