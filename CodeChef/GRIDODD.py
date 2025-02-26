# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    lis = []
    
    r = [0] * n
    val = 1
    for i in range(0, n, 2):
        r[i] = val
        val+=1
    for i in range(1, n, 2):
        r[i] = val
        val += 1
    
    for i in range(n):
        lis.append(r)
        r = r[1:] + r[:1]
    
    for i in lis:
        print(*i)