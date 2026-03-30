# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # dfs and track the max on root -> curr
        # no edge case as root is not None
        def dfs(cur, prev_max, count):
            if cur.val >= prev_max:
                count+=1
                prev_max = cur.val
            if cur.left:
                count = dfs(cur.left,prev_max,count)
            if cur.right:
                count = dfs(cur.right,prev_max,count)
            
            return count
        
        return dfs(root,-101,0)