class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones
        ans = 10**9+7
        for i in range(n):
            x = nums[i]
            for j in range(i+1, n):
                x = gcd(x, nums[j])
                if x == 1:
                    ans = min(ans, j-i)
        if ans == 10**9+7:
            return -1
        return ans + n - 1