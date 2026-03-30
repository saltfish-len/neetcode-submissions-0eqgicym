# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # left-first dfs
        # reduce k as post order for left, pre order for right
        vals = []
        def dfs(cur):
            if cur is None:
                return 
            dfs(cur.left)
            vals.append(cur.val)
            dfs(cur.right)
            return
            
        dfs(root)

        return vals[k-1]