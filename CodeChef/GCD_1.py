# cook your dish here
for h in range(int(input())):
    l=[int(i) for i in input().split()]
    n,m=l[0],l[1]
    mat=[[0]*m for j in range(n)]
    for i in range(n):
        for j in range(m):
            mat[i][j]=(i+1)+(j+1)
    for i in range(n):
        for j in range(m):
            print(mat[i][j],end=" ")
        print()