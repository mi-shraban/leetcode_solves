class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = [[]]
        for x in nums:
            temp = []
            for subset in subsets:
                if subset + [x] not in subsets:
                    temp.append(subset + [x])
            subsets.extend(temp)
        return subsets