def setZeroes(matrix): 
    row =[0 for i in range(len(matrix))]
    cols = [0 for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = -1
                cols[j] =-1
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i]==-1 or cols[j] == -1:
                matrix[i][j] = 0
    
    return matrix


matrix = [[1,1,1],[1,0,1],[1,1,1]]
print(setZeroes(matrix))

# # list comprehension to create a list of indices
# arr = [0 for i in range(len(matrix))]
# print(arr)