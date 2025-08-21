class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # print(chr(ord("A") + 1))
        res = ""
        while columnNumber > 0:
            offset =  (columnNumber - 1) % 26
            # res = chr(ord("A") + offset) + res (if i do it like this i do not have to reverse the output string)
            
            res += chr(ord("A") + offset)
            columnNumber = (columnNumber -1) // 26
        return res[::-1]