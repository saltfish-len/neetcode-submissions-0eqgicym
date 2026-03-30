# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # recursivly, check if current is a CA, return when not a ca
        lval, rval = min(p.val,q.val),max(p.val,q.val)


        def dfs(cur):
            if lval<=cur.val<=rval:
               return cur
            
            if cur.val > rval:
                return dfs(cur.left)
            if cur.val < lval:
                return dfs(cur.right)
            
            return None

        return dfs(root)

        
        
        