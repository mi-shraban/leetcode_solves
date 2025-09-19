# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dumm = ListNode(0)
        dumm.next = head
        prev = dumm
        curr = head
        while curr:
            is_dup = False
            while curr.next and curr.next.val == curr.val:
                is_dup = True
                curr = curr.next
            if is_dup:
                prev.next = curr.next
            else:
                prev = prev.next
            curr = curr.next
        return dumm.next