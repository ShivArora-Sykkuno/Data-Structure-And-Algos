from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        graph_len = len(graph)
        reverse_list = [[] for _ in range(graph_len)]
        ind = [0] * graph_len

        for i in range(graph_len):
            for j in graph[i]:
                reverse_list[j].append(i)
                ind[i] += 1
        
        q = deque()
        for i in range(graph_len):
            if ind[i] == 0:
                q.append(i)
                
        res = [ ]
        while q:
            curr_node = q.popleft()
            res.append(curr_node)
            for adjNode in reverse_list[curr_node]:
                ind[adjNode] -= 1
                if ind[adjNode] == 0:
                    q.append(adjNode)
        return sorted(res)

