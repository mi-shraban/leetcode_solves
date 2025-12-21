class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n, m = len(strs), len(strs[0])
        sorted_flags = [False] * (n-1)
        cnt = 0
        for i in range(m):
            unsorted = False
            for j in range(n-1):
                if not sorted_flags[j] and strs[j][i] > strs[j + 1][i]:
                    unsorted = True
                    break
            if unsorted:
                cnt += 1
                continue
            for j in range(n-1):
                if not sorted_flags[j] and strs[j][i] < strs[j + 1][i]:
                    sorted_flags[j] = True
            if all(sorted_flags):
                break
        return cnt