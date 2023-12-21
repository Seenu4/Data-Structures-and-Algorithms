class MinHeap:
    def __init__(self):
        self.heap = []

    def size(self):
        return len(self.heap)

    def parent(self, index):
        return (index - 1) // 2

    def left_child(self, index):
        return (2 * index) + 1

    def right_child(self, index):
        return (2 * index) + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            self.swap(index, self.parent(index))
            index = self.parent(index)

    def heapify_down(self, index):
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)

        if left < self.size() and self.heap[left][0] < self.heap[min_index][0]:
            min_index = left
        if right < self.size() and self.heap[right][0] < self.heap[min_index][0]:
            min_index = right
        if index != min_index:
            self.swap(index, min_index)
            self.heapify_down(min_index)

    def add(self, value):
        self.heap.append(value)
        self.heapify_up(self.size() - 1)

    def extractMin(self):
        if self.size() == 0:
            return None
        min_element = self.heap[0]
        self.swap(0, self.size() - 1)
        self.heap.pop()
        self.heapify_down(0)
        return min_element

class MatrixGraph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    def add_edge(self, from_vertex, to_vertex, weight):
        self.graph[from_vertex][to_vertex] = weight
        self.graph[to_vertex][from_vertex] = weight  

    def get_edges(self, vertex):
        edges = []
        for i in range(self.num_vertices):
            if self.graph[vertex][i] > 0:
                edges.append([self.graph[vertex][i], vertex, i])
        return edges

def dijkstra(graph):
    visited = set()
    result = []
    heap = MinHeap()

    start_node = 0
    visited.add(start_node)
    edges = graph.get_edges(start_node)
    for edge in edges:
        heap.add(edge)

    while heap.size() > 0:
        shortest = heap.extractMin()
        if shortest is None:
            break

        cost, fr, to = shortest

        if to not in visited:
            result.append(shortest)
            visited.add(to)
            edges = graph.get_edges(to)
            for edge in edges:
                if edge[2] not in visited:
                    heap.add([edge[0] + cost, to, edge[2]])

    return result


graph = MatrixGraph(6) # 6 vertices
graph.add_edge(0,1,3)
graph.add_edge(0,2,6)
graph.add_edge(1,3,2)
graph.add_edge(1,4,8)
graph.add_edge(1,2,13)
graph.add_edge(2,4,7)
graph.add_edge(3,5,12)
graph.add_edge(3,4,26)
graph.add_edge(4,5,5)
# Performing Dijkstra's algorithm
print("The shortest path from the source 1 to all vertices are:\n ",dijkstra(graph)) 
