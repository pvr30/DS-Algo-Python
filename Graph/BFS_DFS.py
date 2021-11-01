"""
BFS:- Breadth First Search
--- BFS is an algorithm for traversing Graph Data structure.
-- It starts at some arbitary node of a graph and explores the neighbour nodes(which are at current level)first, 
    before moving to the next level neighbors.

DFS:- Depth First Search
 -- It starts selecting some arbitary node and explores as far as possible along each track before backtracking


-- Time And Space Complexity Of BSF and DSF is O(vertex + edges)
"""
from collections import deque


class Graph:
    def __init__(self, gdict={}):
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    # BFS - Breadth First Search
    def bfs(self, vertex):
        visited = [vertex] #inislize visited list with root
        queue = deque([vertex]) # queue with root
        while queue:
            # get the vertex one by one by poping from front of queue 
            vertex = queue.popleft()
            # print the breadth order of graph
            print(vertex, end=" ")
            # treverse all adjacent of vertex
            for i in self.gdict[vertex]:
            
                # check if the adjacent element is visited or not.
                if i not in visited:
                    # if not visited then add it to visited
                    visited.append(i)
                    # also append in queue to get vertex
                    queue.append(i)
        print("\n")

    # DFS - Depth First Seach
    def dfs(self, vertex):
        visited = [vertex]  # all the visited element
        stack = [vertex]
        while stack:
            # get the top element of stack
            vertex = stack.pop()
            # print the depth order of graph
            print(vertex, end=" ")
            for i in self.gdict[vertex]:
                if i not in visited:
                    visited.append(i)
                    stack.append(i)
        print("\n")

gdict = {
    0:[1, 2, 3],
    1:[0,2],
    2:[0,1,4],
    3:[0],
    4:[2]
}
graph = Graph(gdict)
graph.bfs(0)

graph.dfs(0)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["d", "f"],
    "f": ["d", "e"]
}

graph2 = Graph(customDict)
graph2.bfs("a")
graph2.dfs("a")