from collections import deque
import math

class SimpleGraph:
    def __init__(self, matrix):  # ← правильно __init__
        if any(len(row) != len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")
        self.matrix = matrix

    def __str__(self):  # ← правильно __str__
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def WarshallAlgorithm(self):
        n = len(self.matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][k] == 1 and self.matrix[k][j] == 1:
                        self.matrix[i][j] = 1

    def FloydWarshallAlhoritm(self):  # можно переименовать на FloydWarshallAlgorithm
        n = len(self.matrix)
        infinity = math.inf

        # Заменяем 0 (где нет ребра) на бесконечность, кроме диагонали
        for i in range(n):
            for j in range(n):
                if i != j and self.matrix[i][j] == 0:
                    self.matrix[i][j] = infinity

        # Основной алгоритм
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][k] != infinity and self.matrix[k][j] != infinity:
                        self.matrix[i][j] = min(self.matrix[i][j], self.matrix[i][k] + self.matrix[k][j])

        return self.matrix

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in range(len(self.matrix[start])):
            if self.matrix[start][neighbor] == 1 and neighbor not in visited:
                self.dfs(neighbor, visited)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)
        while queue:
            node = queue.popleft()
            print(node, end=' ')
            for neighbor in range(len(self.matrix[node])):
                if self.matrix[node][neighbor] == 1 and neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Пример использования:
graph = SimpleGraph([
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0]
])

graph2 = SimpleGraph([
    [0, 3, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 7],
    [2, 0, 0, 0]
])

print("Матрица до алгоритма Воршелла:")
print(graph)

graph.WarshallAlgorithm()

print("\nМатрица после алгоритма Воршелла:")
print(graph)

print("\nDFS с вершины 0:")
graph.dfs(0)

print("\nBFS с вершины 0:")
graph.bfs(0)

shortest_path = graph2.FloydWarshallAlhoritm()
for row in shortest_path:
    print(row)
