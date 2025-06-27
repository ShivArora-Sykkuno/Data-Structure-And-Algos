def amstrong(num):
    count = 0
    tsum = 0
    temp = num
    while temp != 0:
        count += 1
        temp = int(temp/10)

    temp2 = num
    while temp2 != 0:
        tsum += (temp2%10) ** count
        temp2 = int(temp2/10)
    
    if num == tsum:
        return True
    else:
        return False


print(amstrong(53)) 