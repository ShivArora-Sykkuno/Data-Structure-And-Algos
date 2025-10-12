# To tell the maximum sum of a subarray where the sum of the numbers iis a prime number

import math

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def solve(arr, n):
    max_ending_here = 0
    max_prime_sum = 0

    for i in range(n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])

        if isPrime(max_ending_here):
            max_prime_sum = max(max_prime_sum, max_ending_here)

        if max_ending_here < 0:
            max_ending_here = 0

    return max_prime_sum

        

n = int(input("Enter the lenght of the array: "))
arr = list(map(int, input("Enter the array: ").split()))
ans = solve(arr, n)
print(ans)