# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    c=0
    for j in range(2,n+1,2):
        pre= s[:j]
        z= pre.count('0')
        o= pre.count('1')
        if z==o:
            c+= 1
    print(2**c)