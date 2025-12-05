class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        pref = [nums[0]]
        for x in nums[1:]:
            pref.append(pref[-1] + x)
        n = len(nums)
        ans = 0
        for i in range(n-1):
            diff = pref[i] - (pref[n - 1] - pref[i])
            if diff % 2 == 0:
                ans += 1
        return ans