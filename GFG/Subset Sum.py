class Solution:
    def __init__(self):
        self.ans = []
        
    def solve(self, index, total, arr):
        
        if index == len(arr):
            self.ans.append(total)
            return
        self.solve(index+1, total+ arr[index], arr) 
        self.solve(index+1, total, arr)
    
    def subsetSums(self, arr):
	    self.solve(0, 0, arr)
	    return self.ans