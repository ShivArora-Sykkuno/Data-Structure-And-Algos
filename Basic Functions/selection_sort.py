def selection_sort(arr):
    min_index = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]     #? Swapping
        min_index = i+1
    return arr

a = [2,6,8,5,3,1]
# selection_sort(a)
print(selection_sort(a))