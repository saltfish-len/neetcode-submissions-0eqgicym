# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node,low,high):
            if node is None:
                return True
            
            if node.left and node.right:
                if low < node.left.val < node.val < node.right.val < high:
                    return dfs(node.left,low,node.val) and dfs(node.right,node.val,high)
                else:
                    return False
            if node.left:
                if low < node.left.val < node.val:
                    return dfs(node.left,low,node.val)
                else:
                    return False
            if node.right:
                if node.val < node.right.val < high:
                    return dfs(node.right,node.val,high)
                else:
                    return False
            return True
            
        return dfs(root,-1000000001,1000000001)
