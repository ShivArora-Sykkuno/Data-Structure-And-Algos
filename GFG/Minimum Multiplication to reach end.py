from collections import deque
from typing import List
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        Mod = 100000
        res = [float("inf") for _ in range(Mod)]
        
        pq = deque()
        pq.append((0, start))
        while pq:
            count, num = pq.popleft()
            if num == end:
                return count
            for adjNum in arr:
                new_num = (num * adjNum) % Mod
                new_count = count + 1
                if new_count < res[new_num]:
                    pq.append((count+1, new_num))
                    res[new_num] = new_count
        
        return -1