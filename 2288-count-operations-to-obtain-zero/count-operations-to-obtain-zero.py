class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        def sub(a, b):
            if a >= b:
                return a - b, b
            else:
                return a, b - a
        cnt = 0
        while num1 != 0 and num2 != 0:
            num1, num2 = sub(num1, num2)
            cnt += 1
        return cnt