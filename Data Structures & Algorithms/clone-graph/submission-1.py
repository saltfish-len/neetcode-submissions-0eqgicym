"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old2new = {}

        def dfs(node):
            # visited
            if node in old2new:
                return old2new[node]
            
            # travesal
            copy = Node(node.val)
            old2new[node] = copy
            for ch in node.neighbors:
                copy.neighbors.append(dfs(ch))
            return copy
        
        return dfs(node) if node else None
        

        