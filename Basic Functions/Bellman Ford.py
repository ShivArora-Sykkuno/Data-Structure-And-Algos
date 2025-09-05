def bellman_ford(edges, src, dst, n): # n is number of vertices and edges input should be the edges list
    distance = [float("inf") for _ in range(n)]
    
    for _ in range(n):
        for u, v, wt in edges:
            if distance[u] != float("inf"):
                if distance[u] + wt < distance[v]:
                    distance[v] = distance[u] + wt
    return distance
