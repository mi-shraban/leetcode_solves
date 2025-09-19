class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def stacc(s):
            l = []
            for x in s:
                if l and x == "#":
                    l.pop()
                elif x != "#":
                    l.append(x)
            return l
        return stacc(s) == stacc(t)
        # O(n), O(n)