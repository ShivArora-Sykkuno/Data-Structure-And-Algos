# cook your dish here

for _ in range(int(input())):
    ones, twos = map(int, input().split())

    print("1" * (ones // 2) + "2" * twos + "1" * (ones // 2))