class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        idx, d = 0, 1
        rows = [[] for _ in range(numRows)]
        for x in s:
            rows[idx].append(x)
            if idx == 0:
                d = 1
            elif idx == numRows-1:
                d = -1
            idx += d
        rows = [f"{''.join(x)}" for x in rows]
        return f"{''.join(rows)}"