

class Graph:
    def __init__(self, gdict={}):
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)


customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
print(graph.gdict)
graph.addEdge("e", "c")
print(graph.gdict["e"])