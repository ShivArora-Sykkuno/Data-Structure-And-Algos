from collections import deque
from copy import deepcopy

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1
                
        grid_cpy = deepcopy(grid)
        directions = [(0,1), (1,0), (-1, 0), (0, -1)]
        minutes = 0
        while q and fresh_oranges > 0:
            minutes += 1
            total_rotten = len(q)
            for _ in range(total_rotten):
                i, j = q.popleft()
                for r, c in directions:
                    new_i = i + r
                    new_j = j + c 

                    if  new_i == rows or new_i < 0 or new_j == cols or new_j < 0:
                        continue
                    if grid_cpy[new_i][new_j] == 2 or grid_cpy[new_i][new_j] == 0:
                        continue
                    grid_cpy[new_i][new_j] = 2
                    fresh_oranges -= 1 
                    q.append((new_i, new_j))
        if fresh_oranges > 0:
            return -1
        else:
            return minutes
