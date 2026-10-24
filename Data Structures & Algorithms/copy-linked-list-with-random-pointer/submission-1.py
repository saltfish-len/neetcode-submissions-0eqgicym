"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # edge case
        if not head:
            return head
        # first pass 
        cur = head
        newHead = Node(head.val)
        newCur = newHead
        link = {} # old:new
        while cur.next:
            link[cur] = newCur # for random
            newCur.val = cur.val
            newCur.next = Node(cur.next.val)
            newCur = newCur.next
            cur = cur.next
        link[cur] = newCur # add last node

        # second pass
        cur = head
        while cur:
            if cur.random is not None:
                link[cur].random = link[cur.random]
            cur = cur.next

        return newHead
