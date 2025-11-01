class Solution:
    def smallestNumber(self, n: int) -> int:
        # ln = 0
        # while n:
        #     n //= 2
        #     ln += 1
        # return (2**ln)-1
        ans = 0
        while ans < n:
            ans *= 2
            ans += 1
        return ans