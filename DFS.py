graph = graph = {
    "13": ["3", "7", "18"],
    "3": ["2", "4", "7"],  
    "7": ["18"],  
    "2": ["4"],
    "4": ["18"],  
    "18": []  
}
def DFS(graph, node):
    stack = [node]
    visited = []

    print("\nOrder of visited nodes by DFS: ", end=" ")

    while stack:
        s = stack.pop()

        if s not in visited:
            visited.append(s)
            print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)

DFS(graph, "13")