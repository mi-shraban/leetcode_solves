# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dum = head
        while dum and dum.next:
            if dum.val == dum.next.val:
                dum.next = dum.next.next
            else:
                dum = dum.next
        return head