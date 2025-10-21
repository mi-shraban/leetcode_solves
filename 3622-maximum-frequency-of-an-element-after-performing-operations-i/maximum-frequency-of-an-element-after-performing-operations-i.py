class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        mx = max(nums) + k + 2
        freq = [0]*mx
        for x in nums:
            freq[x] += 1
        for i in range(1, mx):
            freq[i] += freq[i-1]
        ans = 0
        for i in range(mx):
            l = max(0, i-k)
            r = min(mx-1, i+k)
            if l:
                total = freq[r] - freq[l-1]
            else:
                total = freq[r]
            if i:
                curr = freq[i] - freq[i-1]
            else:
                curr = freq[i]
            ans = max(ans, curr + min(numOperations, total-curr))
        return ans