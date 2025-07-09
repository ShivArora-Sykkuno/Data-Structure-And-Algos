#brute Force approach
def array_rotate(arr, k):
    for i in range(k):
        arr[:] = [arr[-1]] + arr[ : len(arr)-1]
    return arr

# Optimized approach
def optimal_array_rotate(arr, k):
    rot = k % len(arr) #to handle cases where k is greater than the length of the array
    pos = len(arr) - rot # Find the split position
    return arr[pos:] + arr[:pos]

a = [3,9,5,6,7,2]
print(array_rotate(a, 3))
