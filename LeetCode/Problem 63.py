class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if i ==0 and j == 0:
                    continue
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                
                if i > 0:
                    down = dp[i-1][j]
                else:
                    down = 0
                if j > 0:
                    right = dp[i][j-1]
                else:
                    right = 0
                
                dp[i][j] = down + right
        return dp[rows - 1][cols - 1]
        