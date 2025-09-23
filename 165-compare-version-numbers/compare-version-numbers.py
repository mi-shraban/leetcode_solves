class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split('.')
        v2 = version2.split('.')
        m, n = len(v1), len(v2)
        for i in range(max(m, n)):
            if i < m:
                x = int(v1[i])
            else:
                x = 0
            if i < n:
                y = int(v2[i])
            else:
                y = 0
            if x > y:
                return 1
            if x < y:
                return -1
        return 0