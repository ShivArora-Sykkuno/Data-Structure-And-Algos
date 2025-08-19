class Solution:
    def minPartition(self, N):
        rupee = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        
        remaining_amount = N
        notes_req = []
        n = len(rupee) - 1
        
        while n >= 0:
            if rupee[n] <= remaining_amount:
                notes_req.append(rupee[n])
                remaining_amount -= rupee[n]
            else:
                n -= 1
        return notes_req
                