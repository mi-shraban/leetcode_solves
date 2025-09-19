# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next
        dummyHead = head
        if dummyHead:
            while dummyHead and dummyHead.next:
                if dummyHead.next.val == val:
                    dummyHead.next = dummyHead.next.next
                else:
                    dummyHead = dummyHead.next
        return head
        