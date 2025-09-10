class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = grid[0][0]

        for i in range(rows):
            for j in range(cols):
                if i == 0 and j == 0:
                    continue

                down = grid[i][j] + dp[i-1][j] if i > 0 else float("inf")
                right = grid[i][j] + dp[i][j-1] if j > 0 else float("inf")
                
                dp[i][j] = min(down, right)
        # print(dp)
        return dp[rows-1][cols-1]