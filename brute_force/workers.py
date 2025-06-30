import sys

def appointments(index, n, matrix, cost, jobs):
    if (index == n):
        return cost
    min_cost = sys.maxsize
    for i in range(n):
        if (not jobs[i]):
            jobs[i] = True
            c = appointments(index + 1, n, matrix, cost + matrix[index][i], jobs)
            min_cost = min(min_cost, c)
            jobs[i] = False
    return min_cost

matrix = [
    [9, 2, 7],
    [6, 4, 3],
    [5, 8, 1]
]

n = len(matrix)
jobs = [False] * n

result = appointments(0, n, matrix, 0, jobs)
print("Минимальная стоимость назначения:", result)