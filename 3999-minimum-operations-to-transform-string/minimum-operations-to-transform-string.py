class Solution:
    def minOperations(self, s: str) -> int:
        arr = [False]*26
        for x in s:
            arr[ord(x) - ord('a')] = True
        ans = 0
        for i in range(1, 26):
            if arr[i]:
                ans = 26 - i
                break
        return ans