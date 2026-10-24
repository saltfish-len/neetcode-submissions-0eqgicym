# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force
        cur = head
        sz = 0
        while cur:
            sz += 1
            cur = cur.next

        ith = sz-n+1
        
        cur = head
        prev = None
        for _ in range(ith-1): #  is prev
            prev = cur
            cur = cur.next
        
        if prev is None:
            # i.e. i-th = 1st
            return cur.next
        else:
            # prev - remove cur - cur.next
            prev.next = cur.next

        return head





