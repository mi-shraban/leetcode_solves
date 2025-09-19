class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vow = {'a': 0}
        mxv = 0
        con = {'z': 0}
        mxc = 0
        for x in s:
            if x in vowels:
                vow[x] = vow.get(x, 0) + 1
                mxv = max(mxv, vow[x])
            else:
                con[x] = con.get(x, 0) + 1
                mxc = max(mxc, con[x])
        return mxv + mxc