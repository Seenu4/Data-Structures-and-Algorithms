class Prims:
    def __init__(self,vertex):
        self.vertex = vertex
        self.data = [[0 for i in range(self.vertex)] for j  in range(self.vertex)]

    def AddEdges(self,src,dest,cost):
        if src == dest:
            print('same')
        else:
            self.data[src][dest] = cost
            self.data[dest][src] = cost

        return self.data

    def Print(self):
        for i in self.data:
            for j in i:
                print(j,end=' ')
            print()

    def GetNeighbour(self,vertex):
        a = []
        for i in range(len(self.data[vertex])):
            if self.data[vertex][i] > 0:
                a.append(i)
        return a

    def weight(self,src,dest):
        return self.data[src][dest]

    def algo(self, source):
        visited_vertices = []
        distances = {i: 999999 for i in range(len(self.data))}
        distances[source] = 0
        temp_distances = {i: distances[i] for i in distances}

        while temp_distances:
            min_distance = 99999
            key = None
            for vertex in temp_distances:
                if temp_distances[vertex] < min_distance:
                    min_distance = temp_distances[vertex]
                    key = vertex
            temp_distances.pop(key)
            if key not in visited_vertices:
                visited_vertices.append(key)
                neighbors = self.GetNeighbour(key)
                for neighbor in neighbors:
                    if (self.weight(key, neighbor) < distances[neighbor]) and (neighbor not in visited_vertices):
                        distances[neighbor] = self.weight(key, neighbor)
                        temp_distances[neighbor] = self.weight(key, neighbor)
        print('weight is ', sum(distances.values()))
        print('path is ', visited_vertices)

g = Prims(6)
g.AddEdges(0, 1, 3)
g.AddEdges(0, 2, 6)
g.AddEdges(1, 3, 2)
g.AddEdges(1, 4, 8)
g.AddEdges(1, 2, 13)
g.AddEdges(2, 4, 7)
g.AddEdges(3, 4, 26)
g.AddEdges(3, 5, 12)
g.AddEdges(4, 5,5)
g.Print()
g.algo(0)