class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(nums)
        pref = [0, 1]
        ans = -1
        j = 0
        window = SortedList()
        for i in range(n):
            window.add(nums[i])
            while j <= i and window[-1] - window[0] > k:
                window.remove(nums[j])
                j += 1
            ans = (pref[-1] - pref[j] + mod) % mod
            pref.append((ans + pref[-1]) % mod)
        return ans