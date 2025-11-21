class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(26):
            x = chr(ord('a') + i)
            st = -1
            end = -1
            for j in range(n):
                if s[j] == x:
                    if st == -1:
                        st = j
                    end = j
            if st == -1 or st == end:
                continue
            st1 = set()
            for j in range(st + 1, end):
                st1.add(s[j])
            ans += len(st1)
        return ans