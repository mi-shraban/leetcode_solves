class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 1
        n = len(digits)
        for i, x in enumerate(digits):
            ans += x * 10**(n-i-1)
        res = []
        while ans:
            res.append(ans % 10)
            ans //= 10
        return res[::-1]