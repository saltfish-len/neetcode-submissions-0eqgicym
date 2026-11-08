# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # diam(node) = max(depth(left)+depth(right),
        #                  depth(left),
        #                  depth(right)) +1
        d = 0
        def dfs(node):
            nonlocal d
            if not node:
                return 0
            leftHeight, rightHeight = dfs(node.left)+1, dfs(node.right)+1

            d = max(leftHeight + rightHeight -1, d)
            return max(dfs(node.left), dfs(node.right))+1

        dfs(root)
        return d-1