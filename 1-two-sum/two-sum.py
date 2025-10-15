class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict:
                return i, num_dict[diff]
            num_dict[nums[i]] = i
        return None
        # for sorted arrays only ;-;
        # l, r = 0, len(nums)-1
        # while l < r:
        #     if nums[l] + nums[r] == target:
        #         return [l, r]
        #     elif nums[l] + nums[r] > target:
        #         r -= 1
        #     elif nums[l] + nums[r] < target:
        #         l += 1
        # return -1