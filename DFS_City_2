 Using a Python dictionary to act as an adjacency list
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
h = []
visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):

    if node not in visited:
        h.append(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph,'Arab')
k=[]
for i in h:
    if i=='Bucharest':
        k.append(i)
        break
    k.append(i)
print(k)


[ The information contained in this communication is confidential and may be legally privileged. It is intended solely for the use of the individual or entity to whom it is addressed and others authorized to receive it.]
