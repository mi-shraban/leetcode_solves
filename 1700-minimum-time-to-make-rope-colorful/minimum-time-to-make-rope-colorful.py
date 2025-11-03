class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans, curr = 0, 0
        n = len(colors)
        for i in range(n):
            if i > 0 and colors[i] != colors[i-1]:
                curr = 0
            if neededTime[i] > curr:
                ans += curr
            else:
                ans += neededTime[i]
            if neededTime[i] > curr:            # keeps track of the highest time in a consecutive color stretch ;-;
                curr = neededTime[i]
        return ans

# using if else statements is faster that using minmax ;-;