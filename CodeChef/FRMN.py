# cook your dish here
for _ in range(int(input())):
    s=int(input())
    ht_lst=list(map(int,input().split()))
    l_pos=[0]*s
    r_pos=[0]*s
    l_pos[0]=0
    for z in range(1,s):
        dff=ht_lst[z]-ht_lst[z-1]
        if z==1:
            l_pos[z]=0
        else:
            prev_dff=ht_lst[z-1]-ht_lst[z-2]
            l_pos[z]=l_pos[z-1]if prev_dff==dff else z-1
    r_pos[s-1]=s-1
    for z in range(s-2,-1,-1):
        dff=ht_lst[z+1]-ht_lst[z]
        if z==s-2:
            r_pos[z]=s-1
        else:
            next_dff=ht_lst[z+2]-ht_lst[z+1]
            r_pos[z]=r_pos[z+1]if next_dff==dff else z+1
    rng=sorted((l_pos[z],r_pos[z])for z in range(s))
    cnt_no_int=0
    for z in range(s):
        lo,hi,pt=0,s,0
        while lo<hi:
            md=(lo+hi)//2
            if rng[md][0]>rng[z][1]:
                hi=md
            else:
                lo=md+1
        pt=lo
        cnt_no_int+=(s-pt)
    tot_pairs=s*(s-1)//2
    res_pairs=tot_pairs-cnt_no_int
    print(res_pairs)