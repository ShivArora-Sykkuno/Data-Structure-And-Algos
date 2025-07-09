def bubble_sort(arr):
    if len (arr) == 0:
        return 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #?Swapping     
    return arr

a = [2,6,8,5,3,1]
# bubble_sort(a)
print(bubble_sort(a))