import heapq as heap

def print_path(parent, src, dest):
    res = [dest] # if res.append(nod) then remove dest
    nod = dest
    while parent[nod] != nod:
        res.append(parent[nod]) # change it to res.append(nod) and uncomment the append 
        nod = parent[nod]
    # res.append(nod)
    return res[::-1] 

def shortest_path(adj_list, src, dest):
    nodes = len(adj_list)
    visited = [float("inf") for _ in range(nodes)]

    parent = [i for i in range(nodes)]
    pq = []
    heap.heappush(pq, [0, src]) #! Distance, node source
    visited[src] = 0
    while pq:
        dist, nod = heap.heappop(pq)
        for adjNode, wt in adj_list[nod]:
            path = dist + wt
            if visited[adjNode] > path:
                heap.heappush(pq, [path, adjNode])
                visited[adjNode] = path
                parent[adjNode] = nod
    # return parent
    return print_path(parent, src, dest)
    # return visited




# adj_list = [
#     [[1,4], [2,4]],
#     [[0,4], [2,2]],
#     [[0,4], [1,2], [3,3], [4,1], [5,6]]
#     [[2,3], [5,2]],
#     [[2,1], [5,3]],
#     [[2,6], [3,2], [4,3]]
# ]
adj_list = [
    [[1, 2], [3, 1]],         # vertex 0
    [[0, 2], [2, 4], [4, 5]], # vertex 1
    [[1, 4], [3, 3], [4, 1]], # vertex 2
    [[0, 1], [2, 3]],         # vertex 3
    [[1, 5], [2, 1]]          # vertex 4
]

src = 0
des = 4
print(shortest_path(adj_list, src, des))