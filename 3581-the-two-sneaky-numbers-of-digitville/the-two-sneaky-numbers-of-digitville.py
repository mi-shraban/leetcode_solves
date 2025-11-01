class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        ans = []
        for x in nums:
            if x in seen:
                ans.append(x)
            seen.add(x)
        return ans