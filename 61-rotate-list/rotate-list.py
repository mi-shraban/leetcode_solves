# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n = 1
        dummy = head
        while dummy.next:
            dummy = dummy.next
            n += 1
        pos = k % n
        if pos == 0:
            return head
        curr = head
        for _ in range(n-pos-1):
            curr = curr.next
        new_head = curr.next
        curr.next = None
        dummy.next = head
        return new_head