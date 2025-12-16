class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        def expand_from_center(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return s[l+1: r]
        max_pal = s[0]
        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)
            if len(odd) > len(max_pal):
                max_pal = odd
            if len(even) > len(max_pal):
                max_pal = even
        return max_pal