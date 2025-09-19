# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # curr = head
        # seen = set()
        # while curr:
        #     if curr not in seen:
        #         seen.add(curr)
        #     else:
        #         return True
        #     curr = curr.next
        # return False
        # Space: O(n)
        if not head:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
        # Space: O(1)