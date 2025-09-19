class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for row in matrix:
        #     l, r = 0, len(row)-1
        #     while l <= r:
        #         mid = (l + r) // 2
        #         if row[mid] == target:
        #             return True
        #         elif row[mid] > target:
        #             r = mid - 1
        #         else:
        #             l = mid + 1
        # return False
        # O(nlogm)
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        r, c = 0, cols-1
        while r < rows and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1
        return False
        # O(n+m)