INF = float('inf')

def floyd(graph):
    V = len(graph)
    dist = [[0]*V for _ in range(V)]

    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] != INF and dist[k][j] != INF and dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


graph = [
    [INF, 5, INF, 25,INF],
    [INF,INF, INF, 10,20],
    [INF, 25, INF, INF,INF],
    [INF, INF, INF, INF,50],
    [INF,INF, 60, INF,INF]
]

result = floyd(graph)
for row in result:
    print(row)