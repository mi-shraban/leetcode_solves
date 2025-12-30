class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        if n < 3 or m < 3:
            return 0
        ans, ch = 0, 0
        for x in range(n-2):
            for y in range(m-2):
                ht = {i:0 if 1 <= i <=9 else 1 for i in range(16)}
                flag = 0
                c, d = 0, 0
                for i in range(3):
                    a, b = 0, 0
                    for j in range(3):
                        val = grid[x+i][y+j]
                        if ht[val] == 1:
                            flag = 1
                            break
                        ht[val] = 1
                        a += val
                        b += grid[x+j][y+i]
                        if i == j:
                            c += grid[x+i][y+j]
                    if i == 0:
                        ch = a
                    if flag or ch != a or  ch!= b:
                        flag = 1
                        break
                    d += grid[x+i][y+(2-i)]
                if flag == 0:
                    if ch == c and ch == d:
                        ans += 1
        return ans