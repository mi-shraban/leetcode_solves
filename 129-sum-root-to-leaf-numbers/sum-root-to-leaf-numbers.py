# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # def DFS(root, path, paths):
        #     if not root:
        #         return
        #     path.append(f"{root.val}")
        #     if not root.left and not root.right:
        #         paths.append(''.join(path))
        #     else:
        #         DFS(root.left, path, paths)
        #         DFS(root.right, path, paths)
        #     path.pop()
        # paths = []
        # DFS(root, [], paths)
        # ans = 0 
        # for x in paths:
        #     ans += int(x)
        # return ans
        # Using code from [Binary Tree Paths]
        def DFS(root, curr):
            if not root:
                return 0
            curr = curr * 10 + root.val
            if not root.left and not root.right:
                return curr
            return DFS(root.left, curr) + DFS(root.right, curr)
        return DFS(root, 0)
        # Using basic DFS