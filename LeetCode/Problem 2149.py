class Solution:
    def rearrangeArray(self, arr: List[int]) -> List[int]:
        result = []
        for i in range(0, len(arr)):
            if arr[i] > 0:
                result.append(arr[i])
                result.append(0)
        temp = 1
        for i in range(len(arr)):
            if arr[i] < 0:
                result[temp] = arr[i]
                temp+=2
        
        return result