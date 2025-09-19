class Solution(object):
    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_dict:
                return i, num_dict[diff]
            num_dict[nums[i]] = i
        return None