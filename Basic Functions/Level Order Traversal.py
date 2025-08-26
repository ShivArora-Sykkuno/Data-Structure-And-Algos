from collections import deque

def BFS(root):
    res = []
    Q = deque()
    Q.append(root)
    while Q:
        e = Q.popleft()
        res.append(e.val)
        if e.left:
            Q.append(e.left)
        if e.right:
            Q.append(e.right)
        
    return res
