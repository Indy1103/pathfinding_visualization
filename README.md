# Graph Visualizer

A Python application that allows users to create, edit, and visualize graphs using depth-first search (DFS) and breadth-first search (BFS) algorithms. The application uses Tkinter for the graphical user interface.

## Features

- Create a graph by adding nodes and edges
- Toggle nodes on and off (useful for testing algorithms)
- Set a starting node for the search algorithms
- Visualize the search algorithms (DFS and BFS) in real-time
- Clear the graph to start over

## Installation

### Prerequisites

- Python 3.x

### Steps

1. Clone the repository or download the source code:

```
git clone https://github.com/yourusername/graph-visualizer.git
```

2. Change into the project directory:

```
cd graph-visualizer
```

## Usage

To run the application, execute the following command from the project directory:

```
python main.py
```

The Graph Visualizer window will open. You can interact with the application using your mouse and keyboard.

### Creating a Graph

1. Click on a node to toggle it on (white) or off (black).
2. Drag from one node to another to create an edge.
3. Press 's' while hovering over a node to set it as the starting node (orange).

### Running Algorithms

1. Select the desired algorithm (DFS or BFS) from the dropdown menu in the control panel.
2. Click the "Start" button to begin the visualization. The nodes visited by the algorithm will turn blue in the order they are visited.

### Clearing the Graph

1. Click the "Clear" button in the control panel to reset the graph.

## Contributing

Please feel free to submit issues and pull requests for new features, bug fixes, or other improvements.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- Tkinter for providing the graphical user interface

