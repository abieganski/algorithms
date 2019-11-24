# The Bellman-Ford algorithm
# Find the shortest paths from the given source node in a weighted directed graph to all other nodes.
# Is able to handle graphs with negative-weight cycles.
class BellmanFord:

    inf = float('inf')

    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges

    def ShortestPaths(self, source):

        # we'll put the distances from the source vertex to all other in this dictionary
        distances = {}

        # initialize all distances with infinity, except from the source vertex to itself, which is 0
        for v in vertices:
            if v == source:
                distances[v] = 0
            else:
                distances[v] = self.inf

        print(distances)

        V = len(self.vertices) # number of vertices in the graph

        # now 'relax' the distances V-1 times
        for i in range(V-1):
            print( "iteration ", i )
            for e in self.edges:
                u = e['u']
                v = e['v']
                w = e['w']
                
                if distances[v] > distances[u] + w:
                    distances[v] = distances[u] + w
                
        # now 'relax' the distances one more time - if you get a shorter distance, this means there's a negative weight cycle
        # i.e. you can shorten at least one of the distances forever by walking the cycle again and again
        print( "negative-weight cycle detection iteration")
        for e in self.edges:
            u = e['u']
            v = e['v']
            w = e['w']
            
            if (distances[u] != self.inf) and (distances[u] + w < distances[v]):
                return 'negative cycle detected'

        return distances
        

# graphs vertices (nodes) -- in reality the number of vertices and the list of all edges is enough
# but just to be explicit -- let's have the vertices listed here
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

# list of graph edges: edge from vertex u to v with weight w
edges = [
    { 'u': 'A', 'v': 'B', 'w':  4 },
    { 'u': 'A', 'v': 'C', 'w': 14 },
    { 'u': 'A', 'v': 'F', 'w': 18 },
    { 'u': 'B', 'v': 'F', 'w': 67 },
    { 'u': 'B', 'v': 'D', 'w': -1 },
    { 'u': 'C', 'v': 'D', 'w':  5 },
    { 'u': 'C', 'v': 'F', 'w': -4 },
    { 'u': 'D', 'v': 'E', 'w':  7 },
    { 'u': 'E', 'v': 'A', 'w':  2 },
    { 'u': 'F', 'v': 'E', 'w':  2 },
    { 'u': 'F', 'v': 'A', 'w': -8 },
    { 'u': 'F', 'v': 'D', 'w':  8 }
]

bellmanFord = BellmanFord(vertices, edges)

shortestPaths = bellmanFord.ShortestPaths(vertices[0])
print(shortestPaths)

