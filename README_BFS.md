# Search_Code-_BFS_-_DFS

Breath-first search (BFS) is an algorithm used for tree traversal on graphs or tree data structures. 
BFS can be easily implemented using recursion and data structures like dictionaries and lists.

The Algorithm
Pick any node, visit the adjacent unvisited vertex, mark it as visited, display it, and insert it in a queue.
If there are no remaining adjacent vertices left, remove the first vertex from the queue.
Repeat step 1 and step 2 until the queue is empty or the desired node is found.

Explanation
Lines 3-10: The illustrated graph is represented using an adjacency list. An easy way to do this in Python is to use a dictionary data structure, where each vertex has a stored list of its adjacent nodes.

Line 12: visited is a list that is used to keep track of visited nodes.

Line 13: queue is a list that is used to keep track of nodes currently in the queue.

Line 29: The arguments of the bfs function are the visited list, the graph in the form of a dictionary, and the starting node A.

Lines 15-26: bfs follows the algorithm described above:

It checks and appends the starting node to the visited list and the queue.
Then, while the queue contains elements, it keeps taking out nodes from the queue, appends the neighbors of that node to the queue if they are unvisited, and marks them as visited.
This continues until the queue is empty.
Time Complexity
Since all of ​the nodes and vertices are visited, the time complexity for BFS on a graph is O(V + E)O(V+E); where VV is the number of vertices and EE is the number of edges.

https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
