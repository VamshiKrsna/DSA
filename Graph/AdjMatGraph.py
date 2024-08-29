class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [[0]*vertices for _ in range(vertices)]
    def add_edge(self,u,v):
        self.graph[u][v] = 1
        self.graph[v][u] = 1
    def display(self):
        for row in self.graph:
            print(" ".join(map(str,row)))
    def dfs(self,start,visited = None):
        if not visited:
            visited = set()
        visited.add(start)
        print(start,end=" ")
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor,visited)


g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,4)
g.add_edge(1,0)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,3)
g.add_edge(3,1)
g.add_edge(3,2)
g.add_edge(3,4)
g.add_edge(4,0)
g.add_edge(4,1)
g.add_edge(4,3)
g.display()
print("\n")
g.dfs(3)