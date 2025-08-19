
class Solution:
    def nextLargerElement(self, arr):
        n = len(arr)
        stack = [] # Monotonic Stack Approach
        res = [-1] * n
        
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            if len(stack) != 0:
                res[i] = stack[-1]
                
            stack.append(arr[i])
        return res
        


