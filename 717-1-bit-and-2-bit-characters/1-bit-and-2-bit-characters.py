class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        n = len(bits)
        curr = 0
        if bits[-1] == 1:
            return False
        while curr < n:
            if bits[curr] == 0:
                if curr == n - 1:
                    return True
                curr += 1
            else:
                curr += 2
        return False
