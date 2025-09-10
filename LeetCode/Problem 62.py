class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _  in range(m)]
        dp[0][0] = 1
        for row in range(m):
            for col in range(n):
                if row == 0 and col == 0:
                    continue

                down = dp[row-1][col] if row > 0 else 0
                right = dp[row][col-1] if col > 0 else 0
                dp[row][col] = down + right
        print(dp)
        return dp[m-1][n-1]
        