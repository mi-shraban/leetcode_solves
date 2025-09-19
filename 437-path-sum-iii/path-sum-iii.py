# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def DFS(root, curr):
            if not root:
                return 0
            curr += root.val
            try:
                cnt = prefix_sums[curr-targetSum]
            except KeyError:
                cnt = 0
            try:
                prefix_sums[curr] += 1
            except KeyError:
                prefix_sums[curr] = 1
            cnt += DFS(root.left, curr)
            cnt += DFS(root.right, curr)
            prefix_sums[curr] -= 1
            return cnt
        prefix_sums = {0: 1}
        return DFS(root, 0)