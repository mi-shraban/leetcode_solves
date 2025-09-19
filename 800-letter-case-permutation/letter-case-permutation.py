class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def DFS(i, subset):
            if i >= len(s):
                res.append(''.join(subset))
                return
            if s[i].isalpha():
                # decision to include s[i] as upper
                subset[i] = s[i].upper()
                DFS(i+1, subset)
                # decision to include s[i] as lower
                subset[i] = s[i].lower()
                DFS(i+1, subset)
            else:
                subset[i] = s[i]
                DFS(i+1, subset)            
        DFS(0, list(s))
        return res