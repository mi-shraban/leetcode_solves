class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = [0]
        ans = -10**18+7
        for x in nums:
            pref.append(pref[-1] + x)
        for i in range(k):
            mx = 0
            for j in range(i, len(nums) - k + 1, k):
                sm = pref[j + k] - pref[j]
                mx = max(sm, mx + sm)
                ans = max(ans, mx)
        return ans