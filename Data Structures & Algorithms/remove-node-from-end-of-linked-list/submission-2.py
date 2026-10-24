# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # two pointer with dist=n
        # fast = slow.(next*n)
        # when fast.next is None, fast is -1st, slow is -(n+1)th

        # use dummy to handle removing head
        dummy = ListNode(0,head)

        slow = dummy
        fast = dummy
        
        for _ in range(n):
            fast = fast.next
        
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return dummy.next
        
        