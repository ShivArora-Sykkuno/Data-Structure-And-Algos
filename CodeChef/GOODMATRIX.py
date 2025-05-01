# cook your dish here
from collections import defaultdict as dd 

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for __ in range(N)] 
    
    ans = 0
    for rd in [-1, 1]:
        for cd in [-1, 1]:
            freq = dd(int)
            for i in range(N):
                for j in range(M):
                    freq[A[i][j] + rd*i + cd*j] += 1 
            ans = max(ans, max(freq.values()))
    print(N*M - ans)
    