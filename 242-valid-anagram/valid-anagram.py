class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs, ht = {}, {}
        for i in range(len(s)):
            hs[s[i]] = hs.get(s[i], 0) + 1
            ht[t[i]] = ht.get(t[i], 0) + 1
        return hs == ht