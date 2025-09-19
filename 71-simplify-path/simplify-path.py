class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        ans = []
        for x in path:
            if x == '' or x == '.':
                continue
            if x == '..':
                if ans:
                    ans.pop()
                continue
            ans.append(x)
        return f"/{'/'.join(ans)}"