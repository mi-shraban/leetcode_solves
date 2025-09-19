class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # sets = set(nums)
        # res = []
        # for i in range(1, n+1):
        #     if i not in sets:
        #         res.append(i)
        # return res

        # oneliner
        sets = set(nums)
        return [i for i in range(1, n+1) if i not in sets]