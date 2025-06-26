def reverse_digit(num):
    rev = ""
    while(num!=0):
        rev += str(num % 10)
        num = int(num / 10)
    return int(rev)

# x = 5329
# print(reverse_digit(x))