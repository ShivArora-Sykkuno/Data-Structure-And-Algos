class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an = len(a)
        ab = len(b)
        if an < ab:
            a = "0"* (ab-an) + a
        elif an > ab:
            b = "0"* (an-ab) + b

        carry = 0
        res = ""
        for i in range(len(a)-1, -1, -1):
            if a[i] == "1" and b[i] == "1":
                if carry == 0:
                    res += "0"
                    carry = 1
                else:
                    res += "1"
            
    
            elif a[i] == "0" and b[i] == "0":
                if carry == 0:
                    res += "0"
                else:
                    res += "1"
                    carry = 0

            elif (a[i] == "1" and b[i] == "0") or (a[i] == "0" and b[i] == "1"):
                if carry == 0:
                    res += "1"
                else:
                    res += "0"
          
                
        if carry == 1:
            res += "1"
        return res[::-1]