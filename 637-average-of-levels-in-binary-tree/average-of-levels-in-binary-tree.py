# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque([root])
        arr = []
        while q:
            sm = 0
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node is not None:
                    sm += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            arr.append(sm/n)
        return arr
