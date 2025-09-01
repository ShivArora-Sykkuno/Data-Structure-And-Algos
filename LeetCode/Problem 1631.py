from collections import deque

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        if rows == 1 and cols == 1:
            return 0
        mini_effort = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        directions = [(1,0), (0, 1), (-1,0), (0, -1)]
        q= deque()
        q.append((0, 0, 0))
        while q:
            r, c, ef = q.popleft()
            for x,y in directions:
                new_r = r + x
                new_c = c + y
                if new_r < 0 or new_r >= rows or new_c < 0 or new_c >= cols:
                    continue
                if ef > mini_effort[new_r][new_c]:
                    continue
                took_eff = abs(heights[new_r][new_c] - heights[r][c])
                max_effort_till_here = max(ef, took_eff)
                if mini_effort[new_r][new_c] > max_effort_till_here:
                    mini_effort[new_r][new_c] = max_effort_till_here
                    q.append((new_r, new_c, max_effort_till_here))

        return mini_effort[rows-1][cols-1]
        
        