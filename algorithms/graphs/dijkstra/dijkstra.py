# The Dijkstra algorithm
# https://www.codingame.com/playgrounds/1608/shortest-paths-with-dijkstras-algorithm/dijkstras-algorithm
class Dijkstra:

    inf = float('inf')

    def __init__(self, adjacencyList):
        self.adjacencyList = adjacencyList

    def ShortestPaths(self, source):

        # initialize all distances with infinity, except from the source vertex to itself, which is 0
        distances = {}
        for v in self.adjacencyList:
            if v == source:
                distances[v] = 0
            else:
                distances[v] = self.inf

        unprocessed = self.adjacencyList.copy()
        shortestPaths = []

        while( unprocessed ):  # while we haven't calculated the shortest path for all vertices
            # pick u from unprocessed with smallest distance
            minDistance = self.inf
            for unp in unprocessed:
                if (distances[unp] < minDistance):
                    minDistance = distances[unp]
                    u = unp
            shortestPaths.append(u)
            unprocessed.pop(u)
            
            # for all vertices adjacent to u
            for key, val in self.adjacencyList[u].items():
                if (distances[u] + val < distances[key]):
                    distances[key] = distances[u] + val
        
        return distances
        

# graph represented as an adjacency list
adjacencyList = {
    'A': {'B':  4, 'C': 14, 'F': 18 },       # the edge from A to B has weight 4, the edge from A to C has weight 14, ...
    'B': {'F': 67, 'D':  1 },
    'C': {'D':  5, 'F':  4 },
    'D': {'E':  7 },
    'E': {'A':  2 },
    'F': {'E':  2, 'A':  8, 'D':  8 }
}

# make the graph undirected (comment this out if you want)
undirectedAL = adjacencyList.copy()
for srcKey, paths in adjacencyList.items():
    for destKey, weight in paths.items():
        undirectedAL[destKey][srcKey] = weight

dijkstra = Dijkstra(undirectedAL)

distances = dijkstra.ShortestPaths('A')
print(distances)

