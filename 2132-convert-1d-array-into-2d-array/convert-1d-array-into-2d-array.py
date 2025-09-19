class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        li = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                li[i][j] = original[i * n + j]
        return li