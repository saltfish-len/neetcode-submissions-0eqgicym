# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def check(node,target):
            if node is None and target is None:
                return True
            if node and target:
                if node.val == target.val:
                    return check(node.left,target.left) and check(node.right,target.right)
            return False

        def dfs(node):
            if not node:
                return False

            if check(node,subRoot):
                return True

            return dfs(node.left) or dfs(node.right)


        return dfs(root)
            
            