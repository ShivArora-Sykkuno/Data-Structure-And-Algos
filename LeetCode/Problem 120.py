class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n  = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[-1] = triangle[-1]

        for i in range(n-2, -1, -1):
            for j in range(0, i+1):
                
                up = triangle[i][j] + dp[i+1][j] # redundant conditions: if i < n-1 else float("inf")
                dia = triangle[i][j] + dp[i+1][j+1] # redundant conditions: if j < i else float("inf")

                dp[i][j] = min(up, dia)
        print(dp)
        return dp[0][0]

        