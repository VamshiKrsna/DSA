from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def display(self):
        
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example Usage:
g = Graph()
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
print("DFS starting from vertex 2:")
g.dfs(2)
print("\n")
g.display()