# cook your dish here
def count_consecutive(x, arr):
    cnt = 0
    num_subarr = 0
    for num in arr:
        if num == x:
            cnt += 1
        else:
            num_subarr += cnt * (cnt + 1) // 2
            cnt = 0

    num_subarr += cnt * (cnt + 1) // 2

    return num_subarr


def subarr_sum(x, arr):
    cnt = 0
    prefix_sum = 0
    mp = {0: 1}

    for num in arr:
        prefix_sum += num
        cnt += mp.get(prefix_sum, 0)
        mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

    return cnt


def subarr_sum_without(x, arr):
    cnt = 0
    prefix_sum = 0
    mp = {0: 1}

    for num in arr:
        if num == x:
            prefix_sum = 0
            mp = {0: 1}
        else:
            prefix_sum += num
            cnt += mp.get(prefix_sum, 0)
            mp[prefix_sum] = mp.get(prefix_sum, 0) + 1

    return cnt


for _ in range(int(input())):

    size = int(input())
    ARR = list(map(int, input().split()))
    result = 0
    result += count_consecutive(1, ARR)
    result += count_consecutive(3, ARR)

    for i in range(size):
        ARR[i] -= 2
    result += subarr_sum(0, ARR) - subarr_sum_without(0, ARR)

    print(result)

