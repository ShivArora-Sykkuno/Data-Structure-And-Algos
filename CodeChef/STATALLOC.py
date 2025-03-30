# cook your dish here

for _ in range(int(input())):
    sz=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    sm=sum(arr)
    for _ in range(int(input())):
        t1,t2=map(int,input().split())
        lo,hi=0,len(arr)
        res=float('inf')
        while lo<hi:
            md=(lo+hi)//2
            if arr[md]>=t1:
                hi=md
            else:
                lo=md+1
        for j in[hi-1,hi]:
            if 0<=j<sz:
                inc=max(0,t1-arr[j])
                adj=max(0,t2-(sm-arr[j]))
                res=min(res,inc+adj)
        print(res if res!=float('inf')else-1)