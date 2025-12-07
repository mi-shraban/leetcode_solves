class Solution:
    def longestPalindrome(self, s: str) -> int:
        odds = 0
        ht = {}
        n = len(s)
        for x in s:
            ht[x] = ht.get(x, 0) + 1
            if ht[x] & 1:
                odds += 1
            else:
                odds -= 1
        if odds > 1:
            return n - odds + 1
        return n
