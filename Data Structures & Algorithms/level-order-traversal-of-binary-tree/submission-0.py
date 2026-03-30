# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        if root is None:
            return []
        queue = [[root,0]]
        res = []
        level = 0
        while queue:
            cur, l = queue.pop(0) # pop the last, so we append cur.right first
            if l == level:
                res.append([])
                level += 1
            res[-1].append(cur.val)

            if cur.left:
                queue.append([cur.left,l+1])
            if cur.right:
                queue.append([cur.right,l+1])
            
        return res
            
            

