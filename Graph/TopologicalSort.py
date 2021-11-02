"""
Topological Sort : The topological sort algorithm takes a directed graph and returns an array of the nodes 
where each node appears before all the nodes it points to. The ordering of the nodes in the array is called
a topological ordering.

 Here's an example: Since node 1 points to nodes 2 and 3, node 1 appears before them in the ordering.


"""



from collections import defaultdict

class Graph:
    def __init__(self, noofvertices):
        self.graph = defaultdict(list)
        self.noofvertices = noofvertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtils(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtils(i, visited, stack)

        # append visited vertex in post order 
        stack.insert(0, v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtils(k, visited, stack)

        print(stack)


customGraph = Graph(8)

customGraph.addEdge("A", "C")
customGraph.addEdge("C", "E")
customGraph.addEdge("E", "H")
customGraph.addEdge("E", "F")
customGraph.addEdge("F", "G")
customGraph.addEdge("B", "D")
customGraph.addEdge("B", "C")
customGraph.addEdge("D", "F")

print(customGraph.graph)
customGraph.topologicalSort()
