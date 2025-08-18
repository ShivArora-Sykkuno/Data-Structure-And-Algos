class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row_find = rows - 1
        print(rows, cols)
        for i in range(rows):
            if matrix[i][0] > target:
                row_find = i-1
                break
            if matrix[i][0] == target:
                return True
        
        for j in range(cols):
            if matrix[row_find][j] == target:
                return True

        return False                

        