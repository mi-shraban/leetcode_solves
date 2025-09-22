class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == '+':
                stack.append(stack.pop() + stack.pop()) # interchangable
            elif x == '*':
                stack.append(stack.pop() * stack.pop())
            elif x == '-':
                b, a = stack.pop(), stack.pop()         # not interchangable
                stack.append(a - b)
            elif x == '/':
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            else:
                stack.append(int(x))
        return stack.pop()