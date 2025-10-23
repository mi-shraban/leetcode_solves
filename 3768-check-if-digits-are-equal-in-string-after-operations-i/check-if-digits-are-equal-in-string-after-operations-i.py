class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s) > 2:
            newS = []
            for i in range(0, len(s)-1):
                if i + 1 < len(s):
                    pair = (int(s[i]) + int(s[i+1])) % 10
                else:
                    pair = int(s[i]) % 10
                newS.append(pair)
            s = newS
        return s[0] == s[1]