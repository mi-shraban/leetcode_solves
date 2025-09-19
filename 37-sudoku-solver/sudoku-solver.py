class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.grids = [set() for _ in range(9)]
        self.digs = [str(i) for i in range(1, 10, 1)]
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    self.rows[r].add(board[r][c])
                    self.cols[c].add(board[r][c])
                    grid = (r//3)*3 + (c//3)
                    self.grids[grid].add(board[r][c])
        self.dfs(0, 0)
    def dfs(self, row, col):
        if row == 9:
            return True
        nR, nC = row, col+1
        if nC == 9:
            nR, nC = row + 1, 0
        if self.board[row][col] != ".":
            return self.dfs(nR, nC)
        grid = (row // 3) * 3 + (col // 3)
        for dig in self.digs:
            if dig not in self.rows[row] and dig not in self.cols[col] and dig not in self.grids[grid]:
                self.board[row][col] = dig
                self.rows[row].add(dig)
                self.cols[col].add(dig)
                self.grids[grid].add(dig)
                if self.dfs(nR, nC):
                    return True    
                self.board[row][col] = "."
                self.rows[row].remove(dig)
                self.cols[col].remove(dig)
                self.grids[grid].remove(dig)
        return False