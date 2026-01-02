class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()
        for x in nums:
            if x in seen:
                return x
            seen.add(x)
        # n = len(nums)//2
        # ht = {}
        # for x in nums:
        #     ht[x] = ht.get(x, 0) + 1
        # for k, v in ht.items():
        #     if v == n:
        #         return k