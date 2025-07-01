from collections import deque

class SimpleGraph:  # Граф, заданный матрицей смежности
    def init(self, matrix):
        if any(len(row) != len(matrix) for row in matrix):
            raise ValueError("Matrix must be square")
        self.matrix = matrix

    def str(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

    def WarshallAlgorithm(self):
        n = len(self.matrix)
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if self.matrix[i][k] == 1 and self.matrix[k][j] == 1:
                        self.matrix[i][j] = 1

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        # Перебираем все возможные соседние вершины по индексам
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
            # Перебираем все возможные соседние вершины по индексам
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

print("Матрица до алгоритма Воршелла:")
print(graph)

graph.WarshallAlgorithm()

print("\nМатрица после алгоритма Воршелла:")
print(graph)

print("\nDFS с вершины 0:")
graph.dfs(0)

print("\nBFS с вершины 0:")
graph.bfs(0)