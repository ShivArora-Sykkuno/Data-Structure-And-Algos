# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def solve(self, root, res):
        if root == None:
            return
        res.append(root.val)
        self.solve(root.left, res)
        self.solve(root.right, res)
        
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.solve(root, res)
        return res
        