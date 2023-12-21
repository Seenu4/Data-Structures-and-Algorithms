graph = {
    "27": ["45", "67", "17"],
    "45": ["29", "36", "67"],
    "67": ["17"],
    "29": ["36"],
    "36": ["17"],
    "17": []
}

def BFS(graph, node):
    queue = [node]
    visited = [node]

    print("\nOrder of visited nodes by BFS: ", end=" ")

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

BFS(graph, "27")