import sys
from typing import List
sys.setrecursionlimit(10**8)
class Solution:
    def dfs(self, r, c, grid, visited, rows, cols, temp_shape, base_r, base_c):
        if r < 0 or c < 0 or r >= rows or c >= cols:
            return
        if grid[r][c] == 0:
            return
        if visited[r][c] == 1:
            return
        visited[r][c] = 1
        temp_shape.append((r-base_r, c- base_c))
        self.dfs(r+1, c, grid, visited, rows, cols, temp_shape, base_r, base_c)
        self.dfs(r-1, c, grid, visited, rows, cols, temp_shape, base_r, base_c)
        self.dfs(r, c+1, grid, visited, rows, cols, temp_shape, base_r, base_c)
        self.dfs(r, c-1, grid, visited, rows, cols, temp_shape, base_r, base_c)
        
    def countDistinctIslands(self, grid : List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        shapes = set()
        # q = 
        for r in range(rows):
            for c in range(cols):
                if visited[r][c] == 0 and grid[r][c] == 1:
                    temp_shape = []
                    self.dfs(r, c, grid, visited, rows, cols, temp_shape, r, c)
                    shapes.add(tuple(temp_shape))
        return len(shapes)
            