class Solution:
    def isPalindrome(self, x: int) -> bool:
        # s = str(x)
        # n = len(s)
        # for i in range(n//2):
        #     if s[i] != s[n-1-i]:
        #         return False
        # return True
        # string solution
        if x < 0:
            return False
        n = x
        rev = 0
        while x:
            rev *= 10 
            rev += x % 10
            x //= 10
        return n == rev
        # math solution