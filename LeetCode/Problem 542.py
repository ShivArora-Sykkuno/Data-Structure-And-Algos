from collections import deque

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        q = deque()
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    q.append([i, j, 0])

        directions =  [(0,1), (1, 0), (-1, 0), (0, -1)]
        distance_mat = [[0 for _ in range(cols)] for _ in range(rows)]
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        while q:
            i, j, d = q.popleft()
            distance_mat[i][j] = d
            for dx, dy in directions:
                new_i = i + dx
                new_j = j + dy
                if new_i == rows or new_i < 0 or new_j == cols or new_j < 0:
                    continue
                if visited[new_i][new_j]==1:
                    continue
                if mat[new_i][new_j] == 0: # if in original it is 0 then why look for ist distance
                    continue
                visited[new_i][new_j] = 1
                q.append([new_i, new_j, d+1])
        return distance_mat
