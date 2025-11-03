class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [0]*26
        for x in s:
            freq[ord(x)%97] += 1
        mx, mn = 0, 10**8
        for i in range(26):
            if freq[i] % 2 != 0:
                mx = max(mx, freq[i])
            if freq[i] % 2 == 0 and freq[i] > 0:
                mn = min(mn, freq[i])
        return mx - mn