class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # github_upload
        ch_idx = {}
        ans = 0
        start = 0
        for end, ch in enumerate(s):
            if ch in ch_idx and ch_idx[ch] >= start:
                start = ch_idx[ch] + 1
            ch_idx[ch] = end
            ans = max(ans, end - start + 1)
        return ans