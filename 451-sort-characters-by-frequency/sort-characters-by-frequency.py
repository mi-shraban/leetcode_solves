class Solution:
    def frequencySort(self, s: str) -> str:
        ht = {}
        for x in s:
            if not x in ht:
                ht[x] = 1
            else:
                ht[x] += 1
        sorted_ht = sorted(ht.items(), key=lambda x: -x[1])     # O(nlogn)
        ans = ""
        for k, v in sorted_ht:
            while v:
                ans += k
                v -= 1
        return ans