class SimpleGraph: #Граф заданный матрицей смежности
    def __init__(self, matrix):
        if any(len(row) != len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")

        self.matrix = matrix

class SimpleGraphList:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def neighbors(self, vertex):
        return self.adjacency_list[vertex]

class IncidenceGraph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.num_vertices = len(matrix)
        self.num_edges = len(matrix[0]) if matrix else 0

graph = SimpleGraphList([[1, 2] , [4, 5, 6], [7, 8, 9]])

print(graph)