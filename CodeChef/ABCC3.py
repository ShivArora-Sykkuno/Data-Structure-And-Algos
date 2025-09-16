# cook your dish here

for _ in range(int(input())):
    num = int(input())
    str = input()

    a, b = [0 for _ in range(num)], []
    for i in range(num):
        a[i] = a[i - 1] + (1 if str[i] == 'a' else 0)
        if (str[i] == 'b'):
            b.append(i)

    c = [0 for _ in range(num + 1)]
    for i in range(num - 1, -1, -1):
        c[i] = c[i + 1] + (1 if str[i] == 'c' else 0)

    res = float('inf')
    for i in range(1, len(b)):
        res = min(res, a[b[i - 1]] + c[b[i]])
    if (len(b) != 0):
        res = min(res, c[b[0]], a[b[-1]])
    else:
        res = 0
    print(res)