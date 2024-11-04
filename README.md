# Exercise 1
Initializes a queue with the starting point and a set to keep track of visited nodes.
Constantly dequeues paths from the queue, checking if the last node of each path is the goal.
If not the goal and not visited, it adds all neighbors to the path and enqueues the new path.
Returns the path when the goal is found.

# Exercise 2
Uses Depth-First Search to detect cycles.
Maintains two sets: visiting nodes currently in the execution stack and visited nodes that have been fully explored.
If a node is encountered in visiting, a cycle is detected.

# Exercise 3
Employs a priority queue to explore the graph based on the shortest known distances.
Builds the shortest path from the end node back to the start node using the recorded shortest paths.

# Exercise 4
Uses BFS to determine if the graph can be colored using two colors such that no two adjacent nodes have the same color.