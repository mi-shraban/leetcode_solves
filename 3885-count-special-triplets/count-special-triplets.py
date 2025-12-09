class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        mod = 10**9+7
        n = len(nums)
        r, l = {}, {}
        ans = 0
        for x in nums:
            r[x] = r.get(x, 0) + 1
        for j in range(n):
            mid = nums[j]
            r[mid] -= 1
            i = l.get(2*mid, 0)
            k = r.get(2*mid, 0)
            ans = (ans + 1 * i * k) % mod
            l[mid] = l.get(mid, 0) + 1
        return ans