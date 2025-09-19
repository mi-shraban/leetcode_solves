# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        curr = head
        while curr:
            curr = curr.next
            ln += 1
        idx = ln - n
        if idx == 0:
            return head.next
        curr = head
        for i in range(ln-1):
            if i+1 == idx:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head