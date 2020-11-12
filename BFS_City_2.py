graph = {
    'Arab' : ['Sibia','Timisoara','Zerind'],
    'Sibia' : ['Fagaras','Rimnica vilcea'],
    'Fagaras' : ['Bucharest'],
    'Rimnica vilcea' : ['Pitesti'],
    'Pitesti' : ['Bucharest'],
    'Timisoara':  ['Lugoj'],
    'Lugoj':  ['Mehadia'],
    'Mehadia':  ['Dobreta'],
    'Dobreta':  ['Craiova'],
    'Craiova':  ['Pitesti'],
    'Zerind':  ['Oradea'],
    'Oradea':  ['Sibia'],
    'Bucharest': []
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
bfs(visited, graph, 'Arab')
k=[]
for i in h:
    if i=='Bucharest':
        k.append(i)
        break
    k.append(i)
print(k)
