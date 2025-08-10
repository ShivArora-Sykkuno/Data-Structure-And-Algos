class Solution:
    def fib(self, n: int) -> int:
        prev = 0
        nxt = 1
        for i in range(2, n+1):
            prev, nxt = nxt, (prev + nxt)
        
        return nxt if n > 0 else 0