class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.coloring = [-1] * self.num_vertices

    def is_safe(self, vertex, color):
        # Check if the given color is valid for the vertex
        for adjacent_vertex in self.graph[vertex]:
            if self.coloring[adjacent_vertex] == color:
                return False
        return True

    def graph_coloring_util(self, vertex):
        # Base case: If all vertices are colored, return True
        if vertex == self.num_vertices:
            return True

        # Try different colors for the current vertex
        for color in self.colors:
            if self.is_safe(vertex, color):
                self.coloring[vertex] = color

                # Recursively color the remaining vertices
                if self.graph_coloring_util(vertex + 1):
                    return True

                # If coloring with the current color doesn't lead to a solution,
                # backtrack and try the next color
                self.coloring[vertex] = -1

        # If no color can be assigned to the current vertex, return False
        return False

    def graph_coloring(self):
        if self.graph_coloring_util(0):
            # Solution found, print the coloring
            print("Graph coloring found:")
            for vertex, color in enumerate(self.coloring):
                print(f"Vertex {vertex + 1} --> Color {color}")
        else:
            print("No solution exists for the given graph and colors.")


# Example usage
if __name__ == "__main__":
    # Define the graph as an adjacency list
    graph = [
        [1, 2, 3],  # Vertex 0 is adjacent to vertices 1, 2, and 3
        [0, 2],     # Vertex 1 is adjacent to vertices 0 and 2
        [0, 1, 3],  # Vertex 2 is adjacent to vertices 0, 1, and 3
        [0, 2]      # Vertex 3 is adjacent to vertices 0 and 2
    ]

    colors = ["Red", "Green", "Blue"]  # Available colors

    # Create a GraphColoring object and solve the graph coloring problem
    gc = GraphColoring(graph, colors)
    gc.graph_coloring()
