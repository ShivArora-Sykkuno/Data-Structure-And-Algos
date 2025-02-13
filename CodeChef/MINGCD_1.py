# cook your dish here
for _ in range(int(input())):
    n, m = map(int, input().split())
    ans = []
    c = 0

    for i in range(n):
        a = []
        for j in range(m):

            if i == j or (j % n == i) or (i % m == j):
                a.append(3)
            else:
                a.append(2)
        ans.append(a)
    for k in ans:
        print(' '.join(map(str, k)))