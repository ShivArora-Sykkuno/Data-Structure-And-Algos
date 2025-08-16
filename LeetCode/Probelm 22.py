class Solution:
    def __init__(self):
        self.res = []

    def solve(self, index, brackets, total):
        if index >= (len(brackets)):
            if total == 0:
                self.res.append("".join(brackets))
            return
        if total <= -1:
            return
        if  total > (len(brackets) // 2):
            return
        
        brackets[index] = "("
        self.solve(index+1, brackets, total +1)
        brackets[index] = ")"
        self.solve(index+1, brackets, total -1)


    def generateParenthesis(self, nums: int) -> List[str]:
        brackets = [""] * (nums * 2)
        self.solve(0, brackets, 0)
        return self.res
