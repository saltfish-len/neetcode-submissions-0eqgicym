# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # dfs
        if root is None:
            return 0

        def dfs(root,depth):
            if root is None:
                return depth
            if root.left:
                left_depth = dfs(root.left, depth+1)
            else:
                left_depth = depth
            
            if root.right:
                right_depth = dfs(root.right, depth+1)
            else:
                right_depth = depth
            
            return max(left_depth,right_depth)

        depth = dfs(root,1)

        return depth