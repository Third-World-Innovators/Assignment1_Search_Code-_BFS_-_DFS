# Search_Code-_BFS_-_DFS

Depth-first search (DFS), is an algorithm for tree traversal on graph or tree data structures. It can be implemented easily using recursion and data structures like dictionaries 
and sets.

The Algorithm
Pick any node. If it is unvisited, mark it as visited and recur on all its adjacent nodes.
Repeat until all the nodes are visited, or the node to be searched is found.

Explanation
Lines 2-9: The illustrated graph is represented using an adjacency list - an easy way to do it in Python is to use a dictionary data structure. Each vertex has a list of its
adjacent nodes stored.
Line 11: visited is a set that is used to keep track of visited nodes.
Line 21: The dfs function is called and is passed the visited set, the graph in the form of a dictionary, and A, which is the starting node.
Lines 13-18: dfs follows the algorithm described above:
It first checks if the current node is unvisited - if yes, it is appended in the visited set.
Then for each neighbor of the current node, the dfs function is invoked again.
The base case is invoked when all the nodes are visited. The function then returns.
Time Complexity
Since all the nodes and vertices are visited, the average time complexity for DFS on a graph is O(V + E)O(V+E), where VV is the number of vertices and EE is the number of edges. 
In case of DFS on a tree, the time complexity is O(V)O(V), where VV is the number of nodes

https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
