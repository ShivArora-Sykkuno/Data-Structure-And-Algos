for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    m = min(l)
    M = max(l)
    mm = -1
    mx = -1
    for i in range(n-1,-1,-1):
        if l[i]==m:
            mm = max(mm,i)
        if l[i]==M:
            mx = max(mx,i)
    if (mm > mx):
        print(-1)
    else:
        print(n-2)
        for i in range(n-2):
            print(1,3)