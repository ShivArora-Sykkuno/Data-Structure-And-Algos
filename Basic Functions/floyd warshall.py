def floyd_warshall(adj_matirx, n):

    distance_matrix = [[float("inf") for _ in range(n)] for _ in range(n)]
    
    for via in range(n):
        for i in range(n):
            for j in range(n):
                via_distance = distance_matrix[i][via] + distance_matrix[via][j]
                distance_matrix[i][j] = min(distance_matrix[i][j], via_distance)
    return distance_matrix