class Solution:
    def reverse(self, x: int) -> int:
        neg = 1
        if x < 0:
            neg = -1

        t = str(x * neg)
        ans = int(t[::-1]) * neg

        if ans.bit_length() < 32:
            return  ans 
        else:
            return 0