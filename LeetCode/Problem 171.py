class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        # print(ord("Y")-65)  = 24
        res = 0
        n  = len(columnTitle)
        base = 0
        for i in range(n-1, -1, -1):
            x = ord(columnTitle[i]) - 64
            res += x * (26**base)
            base +=1
        return res
