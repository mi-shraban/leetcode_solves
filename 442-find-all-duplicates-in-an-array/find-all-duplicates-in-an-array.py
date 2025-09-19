class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # freq = [0]*(max(nums)+1)
        # res = []
        # for x in nums:
        #     freq[x] += 1
        #     if freq[x] > 1:
        #         res.append(x)
        # return res  
        seen = set()
        ans = []
        for x in nums:
            if x in seen:
                ans.append(x)
            seen.add(x)
        return ans