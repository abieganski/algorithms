# The Dijkstra algorithm
class Dijkstra:

    inf = float('inf')

    def __init__(self, adjacencyList):
        self.adjacencyList = adjacencyList

    def ShortestPaths(self, source):

        # we'll put the distances from the source vertex to all other in this dictionary
        distances = {}

        # initialize all distances with infinity, except from the source vertex to itself, which is 0
        for v in vertices:
            if v == source:
                distances[v] = 0
            else:
                distances[v] = self.inf

        current = source



        return distances
        

# graph represented as an adjacency list
adjacencyList = {
    'A': {'B':  4, 'C': 14, 'F': 18 },       # the edge from A to B has weight 4, the edge from A to C has weight 14, ...
    'B': {'F': 67, 'D':  1 },
    'C': {'D':  5, 'F':  4 },
    'D': {'E':  7},
    'E': {'A':  2},
    'F': {'E':  2, 'A':  8, 'D',  8}
}

dijkstra = Dijkstra(adjacencyList)

shortestPaths = dijkstra.ShortestPaths(vertices[0])
print(shortestPaths)

