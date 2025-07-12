class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        maxi = float('-inf')
        total = 0
        for i in range(len(arr)):
            if total < 0:
                total = 0
            total += arr[i]
            maxi = max(maxi, total)  
        return maxi