class Solution:
    def dfs(self, board, visited, r, c, rows, cols):
        if r < 0 or r == rows  or c < 0 or c == cols:
            return
        if board[r][c] == "X":
            return
        if visited[r][c] == 1:
            return
        visited[r][c] = 1
        # print(visited)

        self.dfs(board, visited, r+1, c, rows, cols)
        self.dfs(board, visited, r-1, c, rows, cols)
        self.dfs(board, visited, r, c+1, rows, cols)
        self.dfs(board, visited, r, c-1, rows, cols)
    
    def solve(self, board: List[:List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        # For Upper row
        for i in range(cols):
            if board[0][i] == "O":
                self.dfs(board, visited, 0, i, rows, cols)
        # For Lower row
        for i in range(cols):
            if board[rows - 1][i] == "O" :
                self.dfs(board, visited, rows - 1, i, rows, cols)
        # For Left column
        for i in range(rows):
            if board[i][0] == "O":
                self.dfs(board, visited, i, 0, rows, cols)
        # For Right column
        for i in range(rows):
            if board[i][cols - 1] == "O":
                self.dfs(board, visited, i, cols - 1, rows, cols)

        # print(visited)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and visited[i][j] == 0:
                    board[i][j] = "X"
