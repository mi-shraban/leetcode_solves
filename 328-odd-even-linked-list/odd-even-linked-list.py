# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        dummy = fast
        while fast and fast.next:
            slow.next = slow.next.next
            fast.next = fast.next.next
            slow = slow.next
            fast = fast.next
        slow.next = dummy
        return head
