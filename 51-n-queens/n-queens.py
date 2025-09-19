class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        state = [['.']*n for _ in range(n)]
        ans = []
        col = set()
        diag = set()
        antidiag = set()
        def backtrack(r):
            if r == n:
                ans.append([''.join(x) for x in state])
            for c in range(n):
                if c in col or (r+c) in antidiag or (r-c) in diag:
                    continue
                state[r][c] = 'Q'
                col.add(c)
                antidiag.add(r+c)
                diag.add(r-c)
                backtrack(r+1)
                state[r][c] = '.'
                col.remove(c)
                antidiag.remove(r+c)
                diag.remove(r-c)
        backtrack(0)
        return ans