class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            temp = 0
            while n:
                temp += (n % 10) ** 2
                n //= 10
            if temp == 1:
                return True
            n = temp
        return False