# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs and for each level, append the last on to result
        if root is None: return []
        queue = [[root,0]]
        res = []
        level = 0
        while queue:
            cur, l = queue.pop(0)
            if l == level:
                # first time this layer
                level+=1
                res.append(cur.val)
            res[l] = cur.val
            if cur.left:
                queue.append([cur.left,l+1])
            if cur.right:
                queue.append([cur.right,l+1])

        return res
        