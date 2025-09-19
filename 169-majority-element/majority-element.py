class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        ans = 1
        for i in range(1, len(nums)):
            if curr != nums[i]:
                ans -= 1
            if ans == 0:
                curr = nums[i]
            if curr == nums[i]:
                ans += 1
        return curr
        # O(n) time, O(1) space