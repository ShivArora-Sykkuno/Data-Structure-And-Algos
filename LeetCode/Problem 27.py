class Solution:
    def removeElement(self, arr: List[int], val: int) -> int:
        index = 0
        for i in range(len(arr)):
            if arr[i] != val:
                arr[index] = arr[i]
                index += 1
        return index