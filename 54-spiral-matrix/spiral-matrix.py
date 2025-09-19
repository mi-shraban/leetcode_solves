class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n, m = len(matrix), len(matrix[0])
        t, b = 0, n - 1
        l, r = 0, m - 1
        ans = []
        while t <= b and l <= r:
            for i in range(l, r + 1, 1):
                ans.append(matrix[t][i])
            t += 1
            for i in range(t, b + 1, 1):
                ans.append(matrix[i][r])
            r -= 1
            if t <= b:
                for i in range(r, l - 1, -1):
                    ans.append(matrix[b][i])
                b -= 1
            if l <= r:
                for i in range(b, t - 1, -1):
                    ans.append(matrix[i][l])
                l += 1
        return ans