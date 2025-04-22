class Solution(object):
    def plusOne(self, digits):
        x = len(digits) - 1
        if digits[x] < 9:
            digits[x] += 1
            return digits
        
        while digits[x] == 9: