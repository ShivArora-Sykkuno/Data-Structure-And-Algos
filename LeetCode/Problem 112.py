# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root, target, total):
        if root == None:
            return False
        
        total += root.val
        if target == total and root.left == None and root.right == None:
            return True
        return self.solve(root.left, target, total) or self.solve(root.right, target, total)

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = self.solve(root, targetSum, 0)
        return res