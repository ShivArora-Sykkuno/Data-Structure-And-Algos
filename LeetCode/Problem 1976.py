import heapq as h
class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        distance = [[] for _ in range(n)]
        for u, v, wt in roads:
            distance[u].append([v, wt])
            distance[v].append([u, wt])

        ways = [0 for _ in range(n)]
        shortest = [float("inf") for _ in range(n)]
        shortest[0] = 0
        ways[0] = 1
        """
        When the cost of traveling from one node to another is differect always try to use 
        priority Queue as it takes the cost as its priority as the push as pop function works as 
        in heap but are costly compared to deque as deque takes O(1) and heap takes O(E logV)
        """
        pq = []
        h.heappush(pq, [0, 0]) 
        while pq:
            cost, node = h.heappop(pq)
            for adjNode, wt in distance[node]:
                path = cost + wt
                if path < shortest[adjNode]:
                    shortest[adjNode] = path
                    ways[adjNode] = ways[node]
                    h.heappush(pq, [path, adjNode])
                elif path == shortest[adjNode]:
                    ways[adjNode] += ways[node]

        return ways[n-1] % (10**9 +7)
