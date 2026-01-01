🧭 Pathfinding Visualizer
Python | Tkinter | Data Structures & Algorithms
📌 Overview:
The Pathfinding Visualizer is an interactive desktop application developed using Python and Tkinter that visually demonstrates how different pathfinding algorithms explore a grid and determine a path between a start and an end point.
The project focuses on understanding graph traversal, algorithm behavior, and path reconstruction through real-time visualization.
🎯 Problem Statement:
Pathfinding algorithms are often difficult to understand when studied only theoretically.
This project provides a visual and interactive way to observe how algorithms work internally, including node exploration, visited states, and final path formation.
✨ Features
Grid-based visualization of a graph
Mouse-based interaction to:
Select start node
Select end node
Create walls (obstacles)
Real-time animation of algorithm execution
Clear visualization of visited nodes and final path
Reset option to test multiple scenarios
🧠 Algorithms Implemented:
Algorithm                               	Description
Breadth-First Search (BFS)	          Finds the shortest path in an unweighted grid
Depth-First Search (DFS)	            Explores paths depth-wise
A*	                                  Uses a heuristic (Manhattan distance) to efficiently compute the shortest path
🧩 Technical Implementation:
Grid represented as a graph of nodes
Each cell acts as a node with dynamically computed neighbors
Efficient data structure usage:
Queue (deque) for BFS
Stack for DFS
Priority Queue (heapq) for A*
Path reconstruction using backtracking
Separation of GUI logic and algorithm logic for maintainability
| Color      | Meaning         |
| ---------- | --------------- |
| White      | Empty cell      |
| Black      | Wall / Obstacle |
| Green      | Start node      |
| Red        | End node        |
| Light Blue | Visited nodes   |


🧪 How to Use:
1. Run the application
2. First click → Set the Start node
3. Second click → Set the End node
4. Additional clicks → Create Walls
5.Click any algorithm button:
   BFS
   DFS
   A*
6.Observe real-time traversal and path visualization
7.Click Reset to clear the grid and try again
⏱ Complexity Analysis:
| Yellow     | Final path      || Algorithm | Time Complexity  | Space Complexity |
| --------- | ---------------- | ---------------- |
| BFS       | O(V + E)         | O(V)             |
| DFS       | O(V + E)         | O(V)             |
| A*        | O(E) (best case) | O(V)             |
Where:
V = number of grid cells
E = number of connections between adjacent cells
📁 Project Structure:
Pathfinding-Visualizer/
│
├── main.py
├── grid.py
├── algorithms.py
├── constants.py
├── README.md
├── .gitignore
│
└── assets/
    └── demo.png   (optional)


