# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    def isSameTree(self, p, q):
        # >> DFS
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
        # >> BFS
        # qp = deque([p])
        # qq = deque([q])
        # while qp and qq:
        #     for _ in range(len(qp)):
        #         np = qp.popleft()
        #         nq = qq.popleft()
        #         if np is None and nq is None:
        #             continue
        #         if np is None or nq is None or np.val != nq.val:
        #             return False
        #         qp.append(np.left)
        #         qp.append(np.right)
        #         qq.append(nq.left)
        #         qq.append(nq.right)
        # return True