class SimpleGraph: #Граф заданный матрицей смежности
    def __init__(self, matrix):
        if any(len(row) != len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")

        self.matrix = matrix

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def WarshallAlgorithm(self):
        n = len(self.matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][k] == 1 and self.matrix[k][j] == 1:
                        self.matrix[i][j] = 1



graph = SimpleGraph([
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
])

print("Матрица до алгоритма Воршелла:")
print(graph)

graph.WarshallAlgorithm()

print("\nМатрица после алгоритма Воршелла:")
print(graph)