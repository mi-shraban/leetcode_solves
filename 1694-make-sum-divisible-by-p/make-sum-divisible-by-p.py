class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        rem = sum(nums)%p
        if rem == 0:
            return 0
        n = len(nums)
        ans = n
        pref_sum = 0
        ht = {0: -1}
        for i, x in enumerate(nums):
            pref_sum += x
            key = (pref_sum % p - rem) % p
            if key in ht:
                ans = min(ans, i-ht[key])
            ht[pref_sum % p] = i
        return ans if ans < n else -1