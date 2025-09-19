class Solution:
    def maximum69Number (self, num: int) -> int:
        n = len(str(num))
        x = 0
        six = False
        ans = num
        for i in range(n):
            if str(num)[i] == '6':
                x = n-i-1
                six = True
                break
        if six:
            ans += 3*(10**x)
        return ans