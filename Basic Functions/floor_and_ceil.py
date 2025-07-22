def fnc(arr, target):
    floor, ceil = -1, len(arr)-1
    low, high = 0, len(arr)-1
    while high >= low:
        mid  = (low + high) // 2 
        if arr[mid] == target:
            floor = mid
            ceil = mid
            break
        if arr[mid] > target:
            floor = mid-1
            ceil = mid
            high = mid-1
        else:
            low = mid+1
    print(f"floor = {arr[floor]} and ceil =  {arr[ceil]}")

arr = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 8
fnc(arr,8)
fnc(arr,11)
fnc(arr,13)
# fnc(arr, 100) #No Floor Value if you want the index then only will work
# fnc(arr, 1) #No Ceil Value if you want the index then only will work
