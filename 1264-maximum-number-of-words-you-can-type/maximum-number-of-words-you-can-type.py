class Solution:
    def canBeTypedWords(self, text: str, broken: str) -> int:
        texts = text.split(' ')
        broken = set(broken)
        ans = len(texts)
        print(ans, texts)
        i = 0
        for i in range(len(texts)):
            for x in texts[i]:
                if x in broken:
                    ans -= 1
                    break
        return ans
                