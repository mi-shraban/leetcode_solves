class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.grid = grid
        self.n = len(self.grid)
        self.m = len(self.grid[0])
        ans = 0
        for i in range(self.n):
            for j in range(self.m):
                if grid[i][j] == '1':
                    self.BFS(i, j)
                    ans += 1
        return ans
    def BFS(self, r, c):
        q = deque()
        q.append((r, c))
        self.grid[r][c] = '#'
        while q:
            x, y = q.popleft()
            moves = ((1, 0), (0, 1), (-1, 0), (0, -1))
            for dx, dy in moves:
                r, c = x + dx, y + dy
                if 0 <= r < self.n and 0 <= c < self.m and self.grid[r][c] == '1':
                        q.append((r, c))
                        self.grid[r][c] = '#'