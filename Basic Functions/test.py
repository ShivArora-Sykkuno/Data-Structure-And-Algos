def findMin(nums):
    low, high = 0, len(nums)-1
    mini = nums[0]
    while high >= low:
        mid = (low + high) // 2
        if nums[mid] >= nums[low]:
            if mini > nums[low]:
                mini = nums[low]
            low = mid + 1
        else:
            if mini > nums[mid]:
                mini = nums[mid]
            high = mid - 1
        
        if nums[mid] == nums[low] == nums[high]:
            low += 1
            high -= 1
            continue

    return mini
    
print(findMin([3,1]))