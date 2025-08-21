class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        temp = [list(row) for row in zip(*matrix)]
        for i in temp:
            i.reverse()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix[i][j] = temp[i][j]
        del temp
        