# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        pid, iid = 0,0
        def dfs(limit):
            nonlocal pid, iid
            if pid >= len(preorder):
                return None
            
            if inorder[iid] == limit:
                iid += 1
                return None
            
            root = TreeNode(preorder[pid])
            pid += 1
            root.left = dfs(root.val)
            root.right = dfs(limit)
            return root
        return dfs(float('inf'))

                
                
