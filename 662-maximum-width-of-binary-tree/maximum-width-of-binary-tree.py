# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        mx_wdth = 0
        q = deque([(root, 0)])
        while q:
            l_idx = q[0][1]
            for i in range(len(q)):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left, 2*idx))
                if node.right:
                    q.append((node.right, 2*idx + 1))
            mx_wdth = max(mx_wdth, idx-l_idx+1)
        return mx_wdth
