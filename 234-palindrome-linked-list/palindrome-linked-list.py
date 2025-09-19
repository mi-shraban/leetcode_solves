# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = None
        while slow:
            temp = slow.next
            slow.next = mid
            mid = slow
            slow = temp
        first, second = head, mid
        while second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        return True