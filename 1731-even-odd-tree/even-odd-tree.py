# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        lvl = 0
        inf = 10**7+7
        while q:
            prev = inf if lvl & 1 else -inf
            for i in range(len(q)):
                curr = q.popleft()
                if (lvl & 1 and (curr.val & 1 or curr.val >= prev)) or (not lvl & 1 and (not curr.val & 1 or curr.val <= prev)):
                    return False
                prev = curr.val  
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            lvl += 1
        return True