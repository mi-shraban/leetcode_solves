class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != '.':
                    idx = i//3 * 3 + j//3
                    if x in row[i] or x in col[j] or x in box[idx]:
                        return False
                    row[i].add(x)
                    col[j].add(x)
                    box[idx].add(x)
        return True