class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        n = len(happiness)
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            if happiness[i] - i <= 0:
                break
            ans += happiness[i] - i
        return ans