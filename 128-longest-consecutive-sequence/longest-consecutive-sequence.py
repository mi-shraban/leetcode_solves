class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n logn)
        # if len(nums) == 0:
        #     return 0
        # curr_l = 1
        # mx_l = 1
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     elif nums[i] - nums[i-1] == 1:
        #         curr_l += 1
        #         mx_l = max(mx_l, curr_l)
        #     else:
        #         curr_l = 1
        # return mx_l
        # O(n)
        hs = set(nums)
        ans = 0
        for x in hs:
            if x-1 not in hs:
                length = 1
                while x + length in hs:
                    length += 1
                ans = max(length, ans)
        return ans