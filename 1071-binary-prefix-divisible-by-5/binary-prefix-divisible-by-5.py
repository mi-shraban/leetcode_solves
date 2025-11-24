class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        val = 0
        for x in nums:
            val = (val * 2 + x) % 5
            ans.append(val == 0)
        return ans