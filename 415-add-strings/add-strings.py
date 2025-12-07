class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        dct = {str(i): i for i in range(10)}
        n, m = len(num1), len(num2)
        if n < m:
            num1 = '0'*(m - n) + num1
        if m < n:
            num2 = '0'*(n - m) + num2
        ans = ""
        carry = 0
        for i in range(max(n, m)-1, -1, -1):
            dgt = dct[num1[i]] + dct[num2[i]] + carry
            carry = 0
            if dgt > 9:
                dgt %= 10
                carry = 1
            ans += str(dgt)
            if i == 0 and carry:
                ans += str(carry)
        return ans[::-1]