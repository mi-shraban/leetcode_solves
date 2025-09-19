# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort here ;-; O(nlogn) time and space.
        if not head or not head.next:
            return head
        mid = self.mid(head)
        left = head
        right = mid.next
        mid.next = None
        return self.merge(self.sortList(left), self.sortList(right))
    def mid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def merge(self, left, right):
        dh = ListNode(0)
        curr = dh
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        if left:
            curr.next = left
        else:
            curr.next = right
        return dh.next