# Using a Python dictionary to act as an adjacency list
graph = {
    'S' : ['c','d','e'],
    'b' : ['i','j','q'],
    'c' : ['e','q'],
    'd' : ['b'],
    'e' : ['f','h'],
    'f':  [],
    'G':  [],
    'h':  [],
    'i':  [],
    'j':  [],
    'p':  ['G'],
    'q':  ['G','p']
}
h = []
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):

    if node not in visited:
        #print (node)
        h.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code

dfs(visited, graph,'S')
k=[]
for i in h:
    if i=='G':
        k.append(i)
        break
    k.append(i)
print(k)
