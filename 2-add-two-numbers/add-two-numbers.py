# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # github_upload
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = cnt = 0
        while l1:
            ans += l1.val*(10**cnt)
            cnt += 1
            l1 = l1.next
        cnt = 0
        while l2:
            ans += l2.val*(10**cnt)
            cnt += 1
            l2 = l2.next
        res = ListNode(0)
        dum = res
        if not ans:
            return ListNode(0)
        while ans:
            num = ans % 10
            dum.next = ListNode(num)
            dum = dum.next
            ans //= 10
        return res.next