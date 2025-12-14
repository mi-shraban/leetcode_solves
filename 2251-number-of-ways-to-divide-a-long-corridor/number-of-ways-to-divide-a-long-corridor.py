class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod = 10**9 + 7
        ans, sc, pc = 1, 0, 0
        for x in corridor:
            if x == 'S':
                sc += 1
            else:
                if sc == 2:
                    pc += 1
            if sc == 3:
                ans = ans * (pc + 1) % mod
                sc, pc = 1, 0
        if sc < 2:
            return 0
        return ans