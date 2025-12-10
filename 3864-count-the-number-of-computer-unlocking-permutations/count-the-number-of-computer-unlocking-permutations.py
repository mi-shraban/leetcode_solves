class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        n = len(complexity)
        ans = 1
        for i in range(1, n):
            if complexity[i] <= complexity[0]:
                return 0
            ans *= i
            ans %= mod
        return ans
        # n-1 factorial is the answer :3 for valid cases.