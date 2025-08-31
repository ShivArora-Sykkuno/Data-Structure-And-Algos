from collections import deque
class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        adj_list =[[] for _ in range(V)]
        indegrees =  [0 for _ in range(V)]
        for v, u in edges:
            adj_list[v].append(u)
            indegrees[u] += 1
        
        q = deque()
        res = []
        for i in range(V):
            if indegrees[i] == 0:
                q.append(i)
            
        while q:
            current_node = q.popleft()
            res.append(current_node)
            for adjNode in adj_list[current_node]:
                indegrees[adjNode] -= 1
                if indegrees[adjNode] ==0:
                    q.append(adjNode)
        return res