class Solution:
    def maxKDistinct(self, nums: List[int], k: int) -> List[int]:
        nums = list(set(nums))
        nums.sort(reverse=True) # length just 100 ;-;
        ans = []
        for i, x in enumerate(nums):
            ans.append(x)
            if i + 1 == k:
                break
        return ans