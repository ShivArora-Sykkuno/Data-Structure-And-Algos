# a = [2,6,8,5,3,1]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]   
        j = i - 1
        while j >= 0 and key < arr[j]:    
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr
    
a = [3,5,6,4,8,9,10,7,1]
# insertion_sort(a)
print(insertion_sort(a))