from collections import deque

def make_adj_lst(lst):
    adj_list = [[]for _ in range(n+1)]
    for u, v in lst:
        adj_list[u].append(v)
        adj_list[v].append(u)
    return adj_list


def bfs(adj_list, n, start_node):
    res =  []
    visited = [0] * (n+1)
    q = deque()
    q.append(start_node)
    visited[start_node] = 1
    while q:
        e = q.popleft()
        res.append(e)
        for node in adj_list[e]:
            if visited[node] == 0:
                q.append(node)
                visited[node] = 1
    return res


def dfs(adj_list, start_node, result, visited):
    result.append(start_node)
    visited[start_node] = 1
    for node in adj_list[start_node]:
        if visited[node] == 0:
            dfs(adj_list, node, result, visited)

    return result





n = int(input("Enter number of vertices: "))
m = int(input("Enter number of edges: "))

#! for taking inputs in the form of u, v as as edge between them (undirected)
lst = []
for i in range(m):
    v, u = map(int, input("Enter the vertices connected: ").split())
    lst.append((v, u))

#! to make the list of those edges into adj list
res = make_adj_lst(lst)

start_node = int(input("Enter the start node for traverasal: "))

BFS = bfs(res, n, start_node)


visited = [0] * (n+1)
DFS  = dfs(res, start_node, [], visited)