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

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

yx= bfs_paths(graph,'Arab','Bucharest')

yo=[]
for i in yx:
    yo.append(i)

def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

x=shortest_path(graph, 'Arab', 'Bucharest')

y=[]
for o in x:
    y.append(o)
print ('\n The possible path(s) to Bucharest from Arab \n')
print (yo)
print('\n The Shortest path is: \n')
print (y)
