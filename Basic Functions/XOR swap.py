def swap(a, b):
    a = a ^ b
    b =  a ^ b
    a = a ^ b
    return a,b

a = 5
b = 10
print(f"Before swap a = {a}, b = {b}")
a, b = swap(a, b)
print(f"After swap a = {a}, b = {b}")