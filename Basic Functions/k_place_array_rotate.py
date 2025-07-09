def array_rotate(arr, k):
    for i in range(k):
        arr[:] = [arr[-1]] + arr[ : len(arr)-1]
    return arr


a = [3,9,5,6,7,2]
print(array_rotate(a, 3))
