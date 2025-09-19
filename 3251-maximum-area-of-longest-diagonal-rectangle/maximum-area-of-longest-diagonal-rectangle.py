class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        mx_diag = 0
        mx_area = 0
        for x, y in dimensions:
            diag = x*x + y*y
            if diag > mx_diag or (diag == mx_diag and x * y > mx_area):
                mx_diag = diag
                mx_area = x * y 
        return mx_area