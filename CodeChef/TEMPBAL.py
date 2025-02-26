# cook your dish here
for _ in range(int(input())):
    n=int(input())
    a=[int(x) for x in input("").split(" ")]
    curr=a[0]
    ans=0
    for i in range(1,n):
        ans+=abs(curr)
        curr=curr+a[i]
    print(ans)