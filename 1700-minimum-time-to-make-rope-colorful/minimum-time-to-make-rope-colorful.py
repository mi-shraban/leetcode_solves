class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, curr = 0, 0
        n = len(colors)
        for i in range(n):
            if i > 0 and colors[i] != colors[i-1]:
                curr = 0
            ans += min(curr, neededTime[i])
            curr = max(curr, neededTime[i])         # keeps track of the highest time in a consecutive color stretch ;-;
        return ans