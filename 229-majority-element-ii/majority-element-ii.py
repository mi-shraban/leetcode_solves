class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ht = {}
        res = set()
        n = len(nums)
        for x in nums:
            ht[x] = ht.get(x, 0) + 1
            if ht[x] > n//3:
                res.add(x)
        return list(res)