class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            res.append(node.val)
            inOrder(node.right)
        inOrder(root)
        return res