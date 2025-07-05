from collections import deque

def count_diamonds_bfs(cave, start_row, start_col):
    if cave[start_row][start_col] == '#':
        return 0  # Старт в стене — мышь не может двигаться

    rows, cols = len(cave), len(cave[0])
    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start_row, start_col)])
    visited[start_row][start_col] = True

    diamonds = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # вверх, вниз, влево, вправо

    while queue:
        r, c = queue.popleft()  # <- Здесь начинается обход BFS (ширина)

        # Собираем алмаз, если он есть
        if cave[r][c] == '*':
            diamonds += 1

        # Проверяем соседей
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (
                    0 <= nr < rows and
                    0 <= nc < cols and
                    not visited[nr][nc] and
                    cave[nr][nc] != '#'
            ):
                visited[nr][nc] = True
                queue.append((nr, nc))  # <- добавляем в очередь новые клетки

    return diamonds

cave = [
    ['0', '*','0', '#', '0','0','0'],
    ['0', '0', '#','#','0','*', '0'],
    ['0', '0', '*','#','0','*', '0'],
    ['*', '*', '0','#','#','#', '#'],
    ['0', '0', '0','0','0','*', '0']
]

start_row = 0
start_col = 4

print(count_diamonds_bfs(cave, start_row, start_col))  # Например, вывод: 3
