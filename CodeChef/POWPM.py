# cook your dish here

for _ in range(int(input())):
    num = int(input())
    notes = list(map(int, input().split()))

    cnt = 0;

    maxx = max(notes)

    for i in range(num):
        if notes[i] == 1:
            cnt += num
            continue
        for j in range(num):
            ele = notes[i] ** (j + 1)
            if ele > maxx:
                break;
            if ele <= notes[j]:
                cnt += 1
            j += 1

    print(cnt)
