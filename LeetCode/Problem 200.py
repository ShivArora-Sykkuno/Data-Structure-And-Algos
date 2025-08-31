class Solution:
    def dfs(self, grid, r, c, visited, rows, cols):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if visited[r][c] == 1:
            return
        if grid[r][c] == "0":
            return
        visited[r][c] = 1
        self.dfs(grid, r+1, c, visited, rows, cols)
        self.dfs(grid, r-1, c, visited, rows, cols)
        self.dfs(grid, r, c+1, visited, rows, cols)
        self.dfs(grid, r, c-1, visited, rows, cols)
         
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited =  [[0 for _ in range(cols)] for _ in range(rows)]
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited[r][c] == 0:
                    count += 1
                    self.dfs(grid, r, c, visited, rows, cols)         
        return count
        