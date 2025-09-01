from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        rows, cols = len(grid), len(grid[0]) 
        # start, end = (0,0), (rows-1, cols-1)
        count = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        q = deque()
        q.append((0, 0, 1)) # r, c, d
        while q:
            r, c, d = q.popleft()
            count[r][c] = d
            directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1,1), (1, -1), (-1, 1), (-1, -1)]
            for x, y in directions:
                new_r = r + x
                new_c = c + y
                if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
                    continue
                if grid[new_r][new_c] == 1:
                    continue
                path = d + 1
                if count[new_r][new_c] > path:
                    count[new_r][new_c] = path
                    q.append((new_r,new_c, path))

        if count[rows-1][cols-1] == float(inf):
            return -1
        else:
            return count[rows-1][cols-1]
        