# cook your dish here

def calc(w1, w2):
    x1, y1 = w1
    x2, y2 = w2
    if x1 == x2:
        d = abs(y1 - y2)
        return (d + 1) // 2 if d % 2 != 0 else d // 2
    elif y1 == y2:
        d = abs(x1 - x2)
        return (d + 1) // 2 if d % 2 != 0 else d // 2
    else:
        return max(abs(x1 - x2), abs(y1 - y2))

def f(p, x):
    if p[x] != x:
        p[x] = f(p, p[x])
    return p[x]

def u_op(p, r, x, y):
    rx = f(p, x)
    ry = f(p, y)
    if rx != ry:
        if r[rx] > r[ry]:
            p[ry] = rx
        elif r[rx] < r[ry]:
            p[rx] = ry
        else:
            p[ry] = rx
            r[rx] += 1

def mt(tc):
    res = []
    for ws in tc:
        n = len(ws)
        e = []
        for i in range(n):
            for j in range(i + 1, n):
                c = calc(ws[i], ws[j])
                e.append((c, i, j))
        e.sort()
        p = list(range(n))
        r = [0] * n
        t = 0
        cc = n
        for c, a, b in e:
            if f(p, a) != f(p, b):
                u_op(p, r, a, b)
                t = max(t, c)
                cc -= 1
                if cc == 1:
                    break
        res.append(t)
    return res
d=0
tc = []
for _ in range(int(input())):
    n = int(input())
    ws = [list(map(int, input().split())) for _ in range(n)]
    tc.append(ws)

ans = mt(tc)
print("\n".join(map(str, ans)))
