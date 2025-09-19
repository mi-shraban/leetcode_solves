class Solution:
    def maxDepth(self, s: str) -> int:
        mx_dep = 0
        dep = 0
        for x in s:
            if x == '(':
                dep += 1
            if x == ')':
                mx_dep = max(mx_dep, dep)
                dep -= 1
        return mx_dep