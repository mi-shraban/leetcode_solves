class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for i in range(4):
            mat = self.rotate(mat)
            if mat == target:
                return True
        return False
    def rotate(self, matrix: List[List[int]]) -> List[List[int]]:
        # inplace transpose
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        #inplace reverse
        for i in range(len(matrix)):
            matrix[i]  = matrix[i][::-1]
        return matrix