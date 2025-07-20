class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = ""
        for i in s:
            if i.isalpha() or i.isdigit():
                temp += i.lower()
        if temp == temp[::-1]:
            return True
        else:
            return False