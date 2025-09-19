class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        ans = [0, 0]
        for i in range(1, n//2+1):
            ans[0] = i
            ans[1] = n - i
            print(ans)
            if '0' not in str(ans[0]) and '0' not in str(ans[1]):
                return ans