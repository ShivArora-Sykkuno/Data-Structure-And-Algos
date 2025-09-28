from collections import deque

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        col_table = {}
        
        q = deque()
        q.append((root, 0, 0))
        while q:
            node, row, col = q.popleft()
            
            # can use defaultdict(list) and skip the initilization
            if col not in col_table:
                col_table[col] = []

            col_table[col].append((row, node.val))
            
            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))

        res = []
        for col in sorted(col_table.keys()):
            nodes_in_col = sorted(col_table[col])
            res.append([val for row, val in nodes_in_col])
        # print(result)
        return res