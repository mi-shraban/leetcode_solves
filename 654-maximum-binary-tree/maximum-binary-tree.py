# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        root, idx = max(nums), nums.index(max(nums))
        left = nums[:idx]
        right = nums[idx+1:]
        tree_root = TreeNode(root)
        tree_root.left = self.constructMaximumBinaryTree(left)
        tree_root.right = self.constructMaximumBinaryTree(right)      
        return tree_root