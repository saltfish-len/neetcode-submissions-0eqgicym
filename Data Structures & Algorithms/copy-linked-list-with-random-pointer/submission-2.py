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
        # magic of defaultdict
        oldToNew = dict()
        oldToNew[None] = None
        cur = head
        while cur:
            oldToNew[cur] = oldToNew.get(cur, Node(0))
            oldToNew[cur].val = cur.val
            oldToNew[cur.next] = oldToNew.get(cur.next, Node(0))
            oldToNew[cur].next = oldToNew[cur.next]
            oldToNew[cur.random] = oldToNew.get(cur.random, Node(0))
            oldToNew[cur].random = oldToNew[cur.random]
            cur = cur.next

        return oldToNew[head]




