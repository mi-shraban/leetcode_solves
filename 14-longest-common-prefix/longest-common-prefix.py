class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        for i in range(len(strs[0])):
            s = strs[0][i]
            for x in strs:
                try:
                    if s != x[i]:
                        return ans
                except IndexError:
                    return ans
            ans += s
        return ans