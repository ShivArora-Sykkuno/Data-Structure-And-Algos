from math import sqrt
def factors(num):
    lst =[]
    for i in range(1, (num//2)+1):  # Check up to num//2 as factors cannot be greater than half of the number
        if num%i == 0:
            lst.append(i)
    lst.append(num)
    return lst



def optimal_factor(num):
    lst =  []
    for i in range(1, int(sqrt(num)+ 1)): # Check up to the square root of num for efficiency as factors come in pairs
        if num % i == 0:
            lst.append(i)
            lst.append(num // i)
    return lst

# print(factors(20))
# print(optimal_factor(20))

# print(factors(36))
# print(optimal_factor(36))