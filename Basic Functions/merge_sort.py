def merge(left, right):
    result = []
    n, m = len(left), len(right)
    i, j = 0, 0

    #? Inserting the elements in the array using sliding window while make the two sorted array into one single sorted array 
    while i<n and j<m:
        if left[i] <= right[j]:
            result.append(left[i])
            i +=1
        else:
            result.append(right[j])
            j+=1

    #? to check and store the remining elements in the merged array if the length of the two array are different
    if i<n:
        while i<n:
            result.append(left[i])
            i+=1
    if j<m:
        while j<m:
            result.append(right[j])
            j+=1
    return result

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    else:
        mid = len(arr)//2
        left_arr = arr[ : mid]
        right_arr = arr[mid : ]
        left = merge_sort(left_arr)
        right = merge_sort(right_arr)
        return merge(left, right)    


a = [3,1,6,2,4,8,7]
print(merge_sort(a))