# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find half
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            old_next = cur.next
            cur.next = prev
            prev = cur
            cur = old_next

        # merge 
        right = prev
        left = head
        while right and left:
            old_left_next = left.next
            old_right_next =  right.next
            left.next = right
            right.next = old_left_next
            left = old_left_next
            right = old_right_next

        