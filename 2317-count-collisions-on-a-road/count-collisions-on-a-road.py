class Solution:
    def countCollisions(self, directions: str) -> int:
        ans = 0
        stack = []
        for x in directions:
            if not stack:
                stack.append(x)
            else:
                top = stack[-1]
                curr = x
                if top == 'R' and x == 'L':
                    ans += 2
                    stack.pop()
                    curr = 'S'
                elif top == 'R' and x == 'S':
                    ans += 1
                    stack.pop()
                    curr = 'S'
                elif top == 'S' and x == 'L':
                    ans += 1
                    stack.pop()
                    curr = 'S'
                while stack and (stack[-1] == 'R' and curr == 'S'):
                    ans += 1
                    stack.pop()
                stack.append(curr)
        return ans
        # stack solve ^^