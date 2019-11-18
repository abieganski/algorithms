inf = float('inf')

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

# we'll put the distances from the source vertex to all other in this dictionary
distances = {}

print( "start")

source = vertices[0] # let's say 'A' is the source vertex

# initialize all distances with infinity, except from the source vertex to itself, which is 0
for v in vertices:
    if v == source:
        distances[v] = 0
    else:
        distances[v] = inf

print(distances)


for i in range(len(vertices)-1):
    print( "iteration ", i )
    for e in edges:
        u = e['u']
        v = e['v']
        w = e['w']
        
        if distances[v] > distances[u] + w:
            distances[v] = distances[u] + w
        
print(distances)

    




