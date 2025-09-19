class Solution:
    def reverse(self, x: int) -> int:
        # if x == 0:
        #     return 0
        # ans = ""
        # if x < 0:
        #     ans = "-"
        #     x = abs(x)
        # while x != 0:
        #     ans += str(x % 10)
        #     x //= 10
        # rev = int(ans)
        # if rev < -2**31 or rev > 2**31-1:
        #     return 0
        # return rev
        # string solution
        ans = 0
        i = -1
        n = abs(x)
        while n:
            n //= 10
            i += 1
        n = abs(x)
        while n:
            ans += (n % 10) * 10**i
            n //= 10
            i -= 1
        print(-2**31, 2**31 - 1)
        if ans > -2147483648 and ans < 2147483647:
            if x < n:
                return -ans
            return ans
        return 0
        # math solution