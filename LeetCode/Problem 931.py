class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[-1] = matrix[-1]
        for i in range(n-2, -1, -1):
            for j in range(n-1, -1, -1):
                
                down = matrix[i][j] + dp[i+1][j]
                if j == n-1:
                    right_dia = float("inf")
                else:
                    right_dia = matrix[i][j] + dp[i+1][j+1]
                    
                if j == 0:
                    left_dia = float("inf")
                else:
                    left_dia = matrix[i][j] + dp[i+1][j-1]
                dp[i][j] = min(down, right_dia, left_dia)
        return min(dp[0])
           
        