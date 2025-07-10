class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(arr)
        i, j= 0 , 1 
        while i < n and j < n:
            if arr[i] == 0 and arr[j] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                i+=1
                j+=1
            elif arr[i]!= 0:
                i+=1
                j+=1
            else:
                j+=1
        