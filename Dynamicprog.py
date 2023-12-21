class Graph:
    def __init__(self, num_vertices):
        self.V = num_vertices
        self.graph = []
        self.nodes = []
        for i in range(self.V):
           self.add_node(i)

    def add_edge(self, start, destination, weight):
        self.graph.append([start, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)

    def print_solution(self, distance):
        print('Vertex distance from source')
        for key, value in distance.items():
            print('  ' + str(key), ' :    ', value)

    def dynamic_prog(self, src):
        distance = {i: float('inf') for i in self.nodes}
        distance[src] = 0
        for _ in range(self.V - 1):
            for start, destination, weight in self.graph:
                if distance[start] != float('inf') and distance[start] + weight < distance[destination]:
                    distance[destination] = distance[start] + weight
        for start, destination, weight in self.graph:
            if distance[start] != float('inf') and distance[start] + weight < distance[destination]:
                print('Graph contains negative cycle')
                return
        self.print_solution(distance)

graph = Graph(6)
graph.add_edge(0, 1, 20)
graph.add_edge(0, 2, 25)
graph.add_edge(1, 3, 35)
graph.add_edge(1, 4, 30)
graph.add_edge(1, 2, 40)
graph.add_edge(2, 4, 45)
graph.add_edge(3, 5, 22)
graph.add_edge(3, 4, 26)
graph.add_edge(4, 5, 50)
graph.dynamic_prog(0)  # Source vertex : 0