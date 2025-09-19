class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        visited = set()
        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        def DFS(k, r, c):
            if k == len(word):
                return True
            if not(0 <= r < n) or not(0 <= c < m) or (r,c) in visited or board[r][c] != word[k]:
                return False
            visited.add((r, c))
            res = False
            for dx, dy in moves:
                res |= DFS(k+1, r+dx, c+dy)
            visited.remove((r, c))
            return res
        for i in range(n):
            for j in range(m):
                if DFS(0, i, j):
                    return True
        return False