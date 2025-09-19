# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def DFS(root, path, paths):
            if not root:
                return
            path.append(f"{root.val}")
            if not root.left and not root.right:
                paths.append('->'.join(path))
            else:
                DFS(root.left, path, paths)
                DFS(root.right, path, paths)
            path.pop()
        paths = []
        DFS(root, [], paths)
        return paths