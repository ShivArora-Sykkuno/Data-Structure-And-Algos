import heapq as hp
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_list = [[] for _ in range(n)]
        for v,u, cost in flights:
            flights_list[v].append([u, cost])
        
        mini_cost = [float("inf") for _ in range(n)]
        pq = []
        #! Have to give priority to distance as the code will not work if not put distance at first in the heap
        # hp.heappush(pq, [0, src, 0]) # distance, source, cost
        hp.heappush(pq, [0, 0, src])
        mini_cost[src] = 0
        while pq:
            # stops, node, c = hp.heappop(pq)
            stops, c, node = hp.heappop(pq)
            for adjNode, wt in flights_list[node]:
                total_cost = c + wt 
                if mini_cost[adjNode] > total_cost and stops <= k:
                    mini_cost[adjNode] = total_cost
                    # hp.heappush(pq, [stops+1, adjNode, total_cost])
                    hp.heappush(pq, [stops+1, total_cost, adjNode])
                     
        if mini_cost[dst] == float("inf"):
            return -1
        else:
            return mini_cost[dst]