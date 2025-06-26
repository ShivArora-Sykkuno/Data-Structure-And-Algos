def frequency(arr):
    freq = {}
    for i in arr:
        if i in freq.keys():
            freq[i] += 1
        else:
            freq[i] = 1
    return freq


# arr = ["apple", "mango", "banana", "apple", "apple"]
# print(frequency(arr))