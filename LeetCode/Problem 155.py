class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        temp_minn = sys.maxsize

        if len(self.stack) == 0:
            temp_minn = val
        else:
            if val < self.stack[-1][1]:
                temp_minn = val
            else:
                temp_minn = self.stack[-1][1]
        self.stack.append([val, temp_minn])
        
        
        
    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        return self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1][1]
    

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()