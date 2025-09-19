# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        q = deque([root])
        while q:
            lvl = []
            for _ in range(len(q)):
                root = q.popleft()
                if root:
                    lvl.append(root.val)
                    q.append(root.left)
                    q.append(root.right)
                else:
                    lvl.append('x')
            print(lvl)
            if not self.isPalindrome(lvl):
                return False
        return True
    def isPalindrome(self, arr):
        l, r = 0, len(arr)-1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l += 1
            r -= 1
        return True