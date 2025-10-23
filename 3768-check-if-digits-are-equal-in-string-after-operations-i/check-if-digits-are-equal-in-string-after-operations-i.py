class Solution:
    def hasSameDigits(self, s: str) -> bool:
        digs = [int(x) for x in s]
        while len(digs) > 2:
            newdigs = []
            for i in range(0, len(digs)-1):
                if i + 1 < len(digs):
                    pair = (digs[i] + digs[i+1]) % 10
                else:
                    pair = digs[i] % 10
                newdigs.append(pair)
            digs = newdigs
        return digs[0] == digs[1]