graph = {
    'Arab': set(['Sibia','Timisoara','Zerind']),
    'Sibia': set(['Fagaras','Rimnica vilcea']),
    'Fagaras': set(['Bucharest']),
    'Rimnica vilcea': set(['Pitesti']),
    'Pitesti': set(['Bucharest']),
    'Timisoara':  set(['Lugoj']),
    'Lugoj':  set(['Mehadia']),
    'Mehadia':  set(['Dobreta']),
    'Dobreta':  set(['Craiova']),
    'Craiova':  set(['Pitesti']),
    'Zerind':  set(['Oradea']),
    'Oradea':  set(['Sibia']),
    'Bucharest': set([])
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

x=list(dfs_paths(graph, 'Arab', 'Bucharest'))
yx=[]
for o in x:
    yx.append(o)

def shortest_path(graph, start, goal):
    try:
        return next(dfs_paths(graph, start, goal))
    except StopIteration:
        return None

x=shortest_path(graph,'Arab','Bucharest') 
y=[]
for o in x:
    y.append(o)
print ('\n The possible path(s) to Bucharest from Arab \n')
print (yx)
print('\n The Shortest path is: \n')
print (y)
