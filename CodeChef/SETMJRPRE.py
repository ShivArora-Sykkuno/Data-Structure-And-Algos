# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    
    ans,x,s=0,0,0
    for i in range(n):
        if l[i]==l[0]:
            s+=1 
        else:
            s-=1
        if s<=0:
            break 
        ans+=s>x 
        x=max(x,s)
    print(ans)