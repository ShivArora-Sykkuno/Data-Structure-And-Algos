class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ch = []
        maxx =  0
        for i in range(len(s)):
            if s[i] in ch:
                indx = ch.index(s[i])
                ch = ch[indx + 1:]
            ch.append(s[i])

            if maxx < len(ch):
                maxx = len(ch)
        return maxx
