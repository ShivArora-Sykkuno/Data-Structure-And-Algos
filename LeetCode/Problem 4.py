class Solution:
    def findMedianSortedArrays(self, num1: List[int], num2: List[int]) -> float :
        num3 = []
        i = 0 
        j = 0
        while i < len(num1) and j < len(num2):
            if num1[i] < num2[j]:
                num3.append(num1[i])
                i += 1
            else:
                num3.append(num2[j])
                j += 1
        
        if i < (len(num1)):
            while i != (len(num1)):
                num3.append(num1[i])
                i += 1
        if j < (len(num2)):
            while j != (len(num2)):
                num3.append(num2[j])
                j += 1

        tot_len = len(num1) + len(num2)
        n = len(num3)//2
        if tot_len % 2 == 0:
            ans = (num3[n]  + num3[n-1]) / 2
            return ans
        else:
            ans = num3[n]
            return ans 