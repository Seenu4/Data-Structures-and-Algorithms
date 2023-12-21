class Graphs:
    def __init__(self, vertex):
        self.vertex = vertex
        self.data = [[0 for i in range(self.vertex)] for j in range(self.vertex)]

    def AddEdges(self, src, dest, cost):
        if src == dest:
            print('same')
        else:
            self.data[src][dest] = cost
            self.data[dest][src] = cost

        return self.data

    def Print(self):
        for i in self.data:
            for j in i:
                print(j, end=' ')
            print()

    def GetNeighbour(self, vertex):
        a = []
        for i in range(len(self.data[vertex])):
            if self.data[vertex][i] > 0:
                a.append(i)
        return a

    def weight(self, src, dest):
        return self.data[src][dest]

    def kruskal(self):
        n = len(self.data)
        edges = []
        for i in range(n):
            for j in range(i + 1, n):
                if self.data[i][j] > 0:
                    edges.append((i, j, self.data[i][j]))
        edges.sort(key=lambda x: x[2])

        mst = []
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[px] = py
                if rank[px] == rank[py]:
                    rank[py] += 1

        for edge in edges:
            if len(mst) == n - 1:
                break
            u, v, weight = edge
            if find(u) != find(v):
                mst.append(edge)
                union(u, v)

        return mst


g = Graphs(6)
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

# Get the minimum spanning tree using Kruskal's algorithm
mst_kruskal = g.kruskal()
print("Minimum Spanning Tree (Kruskal's Algorithm):", mst_kruskal)