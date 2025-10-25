class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7
        d = n % 7
        def sum(x, y):
            return (y*(y+1))//2 - (x*(x+1))//2
        fw = 7 * sum(3, 3+w)    # 3 first week, 3 + wth week
        rd = sum(w, w+d)        # wth week's dth day
        return fw + rd