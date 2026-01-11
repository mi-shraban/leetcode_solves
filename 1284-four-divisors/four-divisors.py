class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            temp = set()
            for i in range(1, int(x**0.5) + 1):
                print(i)
                if x % i == 0:
                    temp.add(x//i)
                    temp.add(i)
                if len(temp) > 4:
                    break
            if len(temp) == 4:
                ans += sum(temp)
        return ans