class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0 
        r_val = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(1, len(s)):
            if r_val[s[i-1]] < r_val[s[i]]:
                ans -= r_val[s[i-1]]
            else:
                ans += r_val[s[i-1]]
        return ans + r_val[s[-1]]