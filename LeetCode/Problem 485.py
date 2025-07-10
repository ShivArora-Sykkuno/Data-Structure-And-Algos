def max_ones(arr):
    total_max = 0
    curr_freq = 0
    for i in range(len(arr)):
        if arr[i] == 1:
            curr_freq +=1
        elif arr[i] == 0:
            if total_max < curr_freq:
                total_max = curr_freq
            curr_freq = 0
    if total_max < curr_freq:
        total_max = curr_freq
    return total_max