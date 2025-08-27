# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        if root  == None:
            return 0
        LS = self.solve(root.left)
        RS = self.solve(root.right)
        return 1 + max(LS , RS)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = self.solve(root)
        return res
        