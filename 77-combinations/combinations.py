class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        com = []
        def dfs(s):
            if len(com) == k:
                ans.append(com.copy())
                return
            for i in range(s, n+1):
                com.append(i)
                dfs(i+1)
                com.pop()
        dfs(1)
        return ans