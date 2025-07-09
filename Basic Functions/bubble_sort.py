def bubble_sort(arr):
    for i in range(len(arr)):
        swap = False
        for j in range(len(arr)-i-1):
            if arr[j]> arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #?Swapping
                swap = True
        if swap == False:
            break     
    return arr

a = [2,6,8,5,3,1]
# bubble_sort(a)
print(bubble_sort(a))