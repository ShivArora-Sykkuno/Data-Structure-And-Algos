class Solution(object):
    def plusOne(self, digits):
        x = len(digits) - 1
        if digits[x] < 9:
            digits[x] += 1
            return digits
        
        while digits[x] == 9:
            digits[x] = 0
            x -= 1 
        if x < 0:
            digits.insert(0, 1)
            return digits
        digits[x] += 1
        return digits  
                
            