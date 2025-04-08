# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    s = input()
    
    cnt = s.count('1')
    
    rev = s[::-1]
    cnt_2 = 0
    for i in rev:
        if i=='0':
            cnt_2 += 1
        
        else:
            break
        
    chance = s.count('0') - cnt_2
    
    if chance >= k:
        chance = k
    
    print(cnt + chance)