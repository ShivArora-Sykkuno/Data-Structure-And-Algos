class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        Word = s.strip().split()
        
        if not Word:
            return 0
        
        return len(Word[-1])