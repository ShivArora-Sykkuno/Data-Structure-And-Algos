class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        ans = []
        i = 0
        sign = 1
        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        while i < len(s) and s[i].isnumeric():
            ans.append(s[i])
            i += 1

        if not ans:
            return 0

        num = int("".join(ans)) * sign

        INT_MIN, INT_MAX = -2147483648, 2147483647
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
        
        return num
        
