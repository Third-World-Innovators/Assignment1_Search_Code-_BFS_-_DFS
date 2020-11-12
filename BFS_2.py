graph = {
  'S': ['c', 'd', 'e'],
  'b': ['i', 'j', 'q'],
  'c': ['e', 'q'],
  'd': ['b'],
  'e': ['f', 'h'],
  'f': [],
  'G': [],
  'h': [],
  'i': [],
  'j': [],
  'p': ['G'],
  'q': ['G', 'p']
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue
h=[]
def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    #print (s, end = " ")
    h.append(s)
    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code
bfs(visited, graph, 'S')
k=[]
for i in h:
    if i=='G':
        k.append(i)
        break
    k.append(i)
print(k)
