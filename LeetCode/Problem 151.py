class Solution:
    def reverseWords(self, s: str) -> str:
        lst = s.split()[::-1]
        res = ""
        for i in lst:
            res = res + i + " "
        return res.strip()