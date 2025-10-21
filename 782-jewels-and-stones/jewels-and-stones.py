class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jw = set([x for x in jewels])
        ans = 0
        for x in stones:
            if x in jw:
                ans += 1
        return ans