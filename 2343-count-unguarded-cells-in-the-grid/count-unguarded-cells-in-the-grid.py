class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        moves = ((1, 0), (0,1), (-1, 0), (0, -1))
        grid = [['u' for i in range(n)] for j in range(m)]
        cnt = n*m
        for x, y in walls:
            grid[x][y] = 'w'
            cnt -= 1
        for x, y in guards:
            grid[x][y] = 'g'
            cnt -= 1
        for x, y in guards:
            for dx, dy in moves:
                ndx, ndy = x + dx, y + dy
                while 0 <= ndx < m and 0 <= ndy < n:
                    if grid[ndx][ndy] == 'g' or grid[ndx][ndy] == 'w':
                        break
                    else:
                        if grid[ndx][ndy] == 'u':
                            grid[ndx][ndy] = 's'
                            cnt -= 1
                    ndx += dx
                    ndy += dy
        return cnt