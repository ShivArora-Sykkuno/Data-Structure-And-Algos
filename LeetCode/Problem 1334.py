class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        distance = [[float("inf") for _ in range(n)] for _ in range(n)]
        for u,v, wt in edges:
            distance[u][v] = wt
            distance[v][u] =wt
        
        for i in range(n):
            distance[i][i] = 0
        
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if distance[i][via] != float("inf") and distance[via][i] != float("inf"):
                        new_via_di = distance[i][via] + distance[via][j]
                        distance[i][j] =min(distance[i][j], new_via_di)
        
        city = -1
        nei = n
        for i in range(n):
            count = 0
            for j in range(n):
                if distance[i][j] <= distanceThreshold:
                    count +=1
            if count <= nei:
                nei = count
                city = i
        return city


        