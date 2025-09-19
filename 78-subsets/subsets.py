class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]
        for x in nums:
            temp = []
            for subset in subsets:
                temp.append(subset + [x])
            subsets.extend(temp)
        return subsets