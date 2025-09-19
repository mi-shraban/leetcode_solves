class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # i = j = k = 0
        # n, m = len(word1), len(word2)
        # ans = ['']*(n+m)
        # while i < n and j < m:
        #     ans[k] = word1[i]
        #     i += 1
        #     k += 1
        #     ans[k] = word2[j]
        #     j += 1
        #     k += 1
        # while i < n:
        #     ans[k] = word1[i]
        #     i += 1
        #     k += 1
        # while j < m:
        #     ans[k] = word2[j]
        #     j += 1
        #     k += 1
        # return f"{''.join(ans)}"
        ans = []
        if len(word1) > len(word2):
            for i in range(len(word2)):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.append(word1[len(word2):])
        else:
            for i in range(len(word1)):
                ans.append(word1[i])
                ans.append(word2[i])
            ans.append(word2[len(word1):])
        return f"{''.join(ans)}"