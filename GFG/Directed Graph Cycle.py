from collections import deque
class Solution:
    def isCycle(self, V, edges):
        # code here
        adj_list = [[] for _ in range(V)]
        ind = [0 for _  in range(V)]
        for v,u in edges:
            adj_list[v].append(u)
            ind[u] += 1
        
        q = deque()
        res = []
        for i in range(V):
            if ind[i] == 0:
                q.append(i)
        
        while q:
            curr_node = q.popleft()
            res.append(curr_node)
            for adjNode in adj_list[curr_node]: # 4, 5
                ind[adjNode] -= 1
                if ind[adjNode] ==0:
                    q.append(adjNode)
        
        if len(res) == V:
            return False
        else:
            return True