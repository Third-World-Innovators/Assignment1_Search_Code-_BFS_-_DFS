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

def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

x=list(dfs_paths(graph, 'S', 'G'))
yx=[]
for o in x:
    yx.append(o)

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None

x=shortest_path(graph,'S','G') # ['A', 'C', 'F']
y=[]
for o in x:
    y.append(o)
print ('\n The possible path(s) to Bucharest from Arab \n')
print (yx)
print('\n The Shortest path is: \n')
print (y)
