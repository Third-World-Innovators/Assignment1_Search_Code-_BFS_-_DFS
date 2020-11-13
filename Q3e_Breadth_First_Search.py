graph = {
    'S' : set(['c','d','e']),
    'b' : set(['i','j','q']),
    'c' : set(['e','q']),
    'd' : set(['b']),
    'e' : set(['f','h']),
    'f':  set([]),
    'G':  set([]),
    'h':  set([]),
    'i':  set([]),
    'j':  set([]),
    'p':  set(['G']),
    'q':  set(['G','p'])
}

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

yx= bfs_paths(graph,'S','G')

yo=[]
for i in yx:
    yo.append(i)

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

x=shortest_path(graph, 'S', 'G')

y=[]
for o in x:
    y.append(o)
print ('\n The possible path(s) to Bucharest from Arab \n')
print (yo)
print('\n The Shortest path is: \n')
print (y)
