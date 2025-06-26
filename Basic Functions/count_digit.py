def count_digits(num):
    count = 0
    while num!=0:
        count +=1
        num = int(num/10)
    return count

x = 342434235252
print(count_digits(x))