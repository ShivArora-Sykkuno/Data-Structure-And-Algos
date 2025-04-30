# cook your dish here
for i in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()))
    maxx = max(arr)
    minn = min(arr)
    if maxx > 0:
        print(maxx, maxx)
    elif maxx == minn == 0:
        print(-1)
    else:
        print(minn, minn)