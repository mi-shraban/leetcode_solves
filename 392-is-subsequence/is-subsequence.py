class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        for x in t:
            if i < len(s) and s[i] == x:
                i += 1
        return i == len(s)