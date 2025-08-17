class Solution:
    def __init__(self):
        # Phone keypad mapping - same as traditional phone buttons
        self.digits_to_letters = {
            "2": "abc",
            "3": "def", 
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        self.res = []
    
    def solve(self, index, sub, digits):
        if len(digits) == 0:
            return
        if index >= len(digits):
            self.res.append("".join(sub))
            return
        for i in self.digits_to_letters[digits[index]]:
            sub.append(i)
            self.solve(index+1, sub, digits)
            sub.pop()


    def letterCombinations(self, digits: str) -> List[str]:
        self.solve(0, [], digits)
        return self.res
       


        