import heapq as Heap

def shortest_path(adj_list, src):
    nodes = len(adj_list)
    visited = [float("inf") for _ in range(nodes)]
    pq = []
    Heap.heappush(pq, [0, src])
    visited[src] = 0
    while pq:
        dist, nod = Heap.heappop(pq)
        for adjNode, wt in adj_list[nod]:
            path = dist + wt
            if visited[adjNode] > path: 
                Heap.heappush(pq, [path, adjNode])
                visited[adjNode] = path
    return visited


adj_list = [
    [[1,4], [2,4]],
    [[0,4], [2,2]],
    [[0,4], [1,2], [3,3], [4,1], [5,6]],
    [[2,3], [5,2]],
    [[2,1], [5,3]],
    [[2,6], [3,2], [4,3]]
]
src = 3
print(shortest_path(adj_list, src))