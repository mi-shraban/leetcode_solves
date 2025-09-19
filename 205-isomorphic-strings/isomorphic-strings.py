class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hs = {}
        ht = {}
        for i in range(len(s)):
            if s[i] not in hs and t[i] not in ht:
                hs[s[i]] = t[i]
                ht[t[i]] = s[i]
            elif hs.get(s[i]) != t[i] or ht.get(t[i]) != s[i]:
                return False
        return True